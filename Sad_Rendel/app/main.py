import os
import math
import traceback

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.responses import Response, RedirectResponse
import psycopg2.errors

from cookies import encrypt_cookie, decrypt_cookie
from db import query_db, close_db_pool

with open('/flag.txt', encoding='ascii') as flag_file:
    FLAG = flag_file.read().strip()

templates = Jinja2Templates(directory='templates')

async def check_user(login, password):
    return await query_db(
        'SELECT id, login from users WHERE login = %s and '
        'password = crypt(%s, password)',
        (login, password),
        results='one'
    )

async def register_user(login, password):
    await query_db(
        "INSERT INTO users (login, password) "
        "VALUES (%s,  crypt(%s, gen_salt('bf')))",
        (login, password)
    )

def get_user(request):
    cookie = request.cookies.get('sess')
    if cookie is None:
        return None
    session_data = decrypt_cookie(cookie)
    return int(session_data["user_id"])


async def index(request):
    user = get_user(request)
    if user is None:
        return RedirectResponse(url='/login',status_code=302)
    return RedirectResponse(url='/user/' + str(user), status_code=302)

async def log_in(request):
    if request.method == 'GET':
        return templates.TemplateResponse('login.html', {'request': request})
    elif request.method == 'POST':
        form = await request.form()
        user_record = await check_user(form['login'], form['password'])
        if user_record is None:
            return templates.TemplateResponse('login.html', {
                'request': request,
                'error': 'Login incorrect, please try again'
            })
        
        user_id = user_record[0]
        cookie = encrypt_cookie({"user_id": user_id})
        response = RedirectResponse("/", status_code=302)
        response.set_cookie("sess", cookie)
        return response

async def log_out(_):
    response = RedirectResponse("/", status_code=302)
    response.delete_cookie("sess")
    return response

async def register(request):
    if request.method == 'GET':
        return templates.TemplateResponse('register.html', {'request': request})
    elif request.method == 'POST':
        form = await request.form()
        login = form['login']
        password = form['password']

        login = login.strip() if login else login
        password = password.strip() if password else password

        if not login or not password:
            return templates.TemplateResponse('register.html', {
                'request': request,
                'error': 'Login or password missing'
            })
        if len(login) > 100:
            return templates.TemplateResponse('register.html', {
                'request': request,
                'error': 'Login too long'
            })
        try:
            await register_user(login, password)
        except psycopg2.errors.UniqueViolation:
            return templates.TemplateResponse('register.html', {
                'request': request,
                'error': 'Such user already exists'
            })
        return templates.TemplateResponse('register_ok.html', {'request': request})


async def get_flag(request):
    user = get_user(request)

    if user is None:
        return templates.TemplateResponse('flag_page.html', {
            'request': request,
            'flag': 'Flag is not available to anonymous users'
        })
    if user == 1:
        return templates.TemplateResponse('flag_page.html', {
            'request': request,
            'flag': FLAG
        })
    else:
        return templates.TemplateResponse('flag_page.html', {
            'request': request,
            'flag': 'Only admin can read a flag'
        })

async def user_profile(request):
    current_user = get_user(request)
    if current_user is None:
        return RedirectResponse(url='/', status_code=302)
    profile_id = request.path_params['user_id']

    user_record = await query_db(
        'SELECT login from users WHERE id = %s', (profile_id,), results='one'
    )
    if user_record is None:
        return templates.TemplateResponse(
            'profile_not_found.html',
            {'request': request},
        )

    is_admin = current_user == 1

    return templates.TemplateResponse('profile.html', {
        'request': request,
        'profile_id': profile_id,
        'current_user': current_user,
        'username': user_record[0],
        'is_admin': is_admin
    })

app = Starlette(
    on_shutdown=[close_db_pool],
    routes=[
        Route('/', endpoint=index),
        Route('/login', endpoint=log_in, methods=["GET", "POST"]),
        Route('/logout', endpoint=log_out),
        Route('/register', endpoint=register, methods=["GET", "POST"]),
        Route('/user/{user_id:int}', user_profile),
        Route('/flag', endpoint=get_flag),
        Mount('/static', StaticFiles(directory='static'), name='static')
    ]
)
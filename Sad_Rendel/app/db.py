import aiopg
import traceback

db_pool = None

async def get_db_pool():
    global db_pool
    if db_pool is None:
        try:
            db_pool = await aiopg.create_pool()
        except:
            traceback.print_exc()
            return None
    return db_pool

async def close_db_pool():
    if db_pool is None:
        return
    db_pool.close()
    await db_pool.wait_closed()

async def query_db(query, params=(), results=None):
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(query, params)
            if results == 'one':
                return await cursor.fetchone()
            if results == 'many':
                return await cursor.fetchall()

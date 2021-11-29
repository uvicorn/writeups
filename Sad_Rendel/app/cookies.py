import os
import json
import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY1 = os.environ['KEY1'].encode('ascii') if 'KEY1' in os.environ else get_random_bytes(32)
KEY2 = os.environ['KEY2'].encode('ascii') if 'KEY2' in os.environ else get_random_bytes(32)


def encrypt_cookie(cookie_data):
    data_json = json.dumps(cookie_data).encode('utf8')
    ctr = AES.new(KEY1, AES.MODE_CTR)
    first_layer = ctr.encrypt(data_json)
    if len(first_layer) % AES.block_size != 0:
        first_layer += b'\0' * (AES.block_size - len(first_layer) % AES.block_size) # pad with zeros
    
    cbc = AES.new(KEY2, AES.MODE_CBC)
    second_layer = cbc.encrypt(first_layer)
    envelope = json.dumps({
        'iv': base64.b64encode(cbc.iv).decode('ascii'),
        'nonce': base64.b64encode(ctr.nonce).decode('ascii'),
        'data': base64.b64encode(second_layer).decode('ascii')
    })

    return base64.b64encode(envelope.encode('ascii')).decode('ascii')

def decrypt_cookie(encrypted_cookie):
    envelope_data = json.loads(base64.b64decode(encrypted_cookie))

    iv = base64.b64decode(envelope_data['iv'])
    cbc = AES.new(KEY2, AES.MODE_CBC, iv)
    second_layer = base64.b64decode(envelope_data['data'])
    first_layer = cbc.decrypt(second_layer)

    nonce = base64.b64decode(envelope_data['nonce'])
    ctr = AES.new(KEY1, AES.MODE_CTR, nonce=nonce)
    data = ctr.decrypt(first_layer)
    return json.JSONDecoder().raw_decode(data.decode('utf8', errors='replace'))[0] # padding with zeros seems to add bad bytes at the end, use raw_decode and `errors='replace'` to ignore them

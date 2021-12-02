I counted only 2 vulnerabilities in this chall.
Here they are:

1. Vulnerable padding function.
```python
BLOCK_SIZE = 32

def pad(data):
    padding_len = (BLOCK_SIZE - len(data)) % BLOCK_SIZE
    return data + bytes([padding_len]*padding_len)
```

The flaw is that a block of the size 32 has nothing added to it ( `pad(b'\x01'*31) == pad(b'\x01'*32)` ).

2. All operations are reversible(From which it follows that the hash can be inverted, and not always in the same plaintext) => Rearrangement of blocks possible.

```python
def cryptohash(msg):
    initial_state = xor(Y_bytes, Z_bytes)
    msg_padded = pad(msg)
    msg_blocks = blocks(msg_padded)
    for i,b in enumerate(msg_blocks):
        mix_in = scramble_block(b)
        ...
        initial_state = xor(initial_state,mix_in) # vuln here
    return initial_state.hex()
```

[Solution using this vulnerability](https://gist.github.com/uvicorn/471f57ff4c55839dd09a21ed0e284a4f)

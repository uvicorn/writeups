from random import *
from base64 import b64decode as dec64

'''
In general, here it was necessary to write a disassembler, 
and then disassemble the algorithm (it is not complicated). 
In total, I spent about 6 hours.
PS: My first solved VM task :3
'''

def ext(*args):
    p('EXIT')
    exit(1)

def beca(st):
    padding = "=" * ((4 - len(st)) % 4)
    mpl = list(dec64(st + padding))
    return mpl


def xor_36(st):
    st = "".join(chr(ord(i) ^ 36) for i in st)
    return st


def sum_chars(st):
    st = sum(ord(i) for i in st)
    return st


def dmagic(xval, st):
    ans = ""
    st = bytes(st.encode())
    for i in range(len(st)):
        ans += chr(st[i] ^ xval)
        xval ^= (ord(ans[i]) | st[i])
    return ans


def add(x1,x2): return x1 + x2
def sub(x1,x2): return x1 - x2
def nop(x1):    return x1


class PUSH:pass
class COPY:pass
class DOUBLE_PACK:pass
class JMP_PLUS:pass
class JNE:pass
class JMP:pass
class _rerere_:pass
class PUSH_PTR:pass
class UNPACK:pass
class PACK:pass

data_memory = [
    [xor_36("Welcome to our CatGirl Industrials shell! There is an offline auth")],
    ["The password is one of the youtube songs.\n"
     "(you can send your favourite song to[REDACTED: to me, @biosergey])\n"],
    [126207464881825709537714540],
    [[_ for _ in reversed(range(10**3))]],
    ["Print the first five symbols of your flag:\n"],
    ["OK, the first block... checking...\n"],
    ["Print the next... six symbols, I suppose:\n"],
    ["Fmmm... Please wait, i'll validate it. Now say about the next nine symbols."],

    [], [], ["YfmkxMuOk6c", "NJou74_9ZXI"]
][::-1]

DEBUG = True
def p(*args):
    global pointer
    if DEBUG:
        print(f"{pointer}>", *args)




inst_memory = [
    print,
    xor_36,
    0,
    JMP_PLUS,
    4,
    ext,
    0,
    print,
    0,
    seed,
    0,
    choice,
    0,
    range,
    0,
    seed,
    0,
    input,
    0,
    COPY,
    len,
    0,
    PUSH,
    5,
    JNE,
    4,
    JMP_PLUS, 4,
    JMP, 5,
    PUSH,
    "youtu",
    JNE,
    4,
    JMP_PLUS, 4,
    JMP, 5,
    PUSH, "Meow!",
    print,
    0,
    print,
    0,
    PUSH, 1,
    PUSH, input,
    _rerere_,
    0,  # input
    0,
    list,
    reversed,
    0,
    PUSH, ['m', 'o', chr(99), chr(46), 'e', chr(98)],
    JNE,
    4,
    JMP_PLUS, 4,
    JMP, 5,
    PUSH, "WOW!",
    print,
    0,
    print,
    0,
    PUSH, "\x0bSEPGL\x1bR\x19",
    nop,
    0,
    PUSH, str(),
    input,
    0,
    nop,
    xor_36,
    nop,
    0,
    JNE, 4,
    JMP_PLUS, 11,  # 0
    JMP, 5,  # 2
    PUSH, "...",
    PUSH, "I have no words",
    JMP_PLUS, 5,
    0,  # 9
    JMP_PLUS, -7,  # 10
    print,
    0,
    print,
    0,
    PUSH, '_6SqP"M/C#N5\x11k\x05k\x1c4T<MeN+Y,\x04f\t|\x06"S*E\'M!S}\x02,\x0cIiS&T O<Uz',
    PUSH, 6,
    DOUBLE_PACK,
    dmagic,
    0,
    print,
    0,
    PUSH, "",
    input,
    0,

    PUSH, -131,  # 112
    PUSH, 1,  # 114
    DOUBLE_PACK,  # 116
    add,  # 117
    0,
    COPY,  # 119
    PUSH, -17,  # 120
    JNE, 4,  # 122
    JMP_PLUS, 8,  # 124
    COPY,  # 126
    PUSH, 0,  # 127
    _rerere_,  # 129
    JMP_PLUS, -16,  # 130
    PUSH, "Ara-ara!",  # 132

    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 0, DOUBLE_PACK, add, 0,
    PUSH, print, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 31, DOUBLE_PACK, add, 0,
    PUSH, print, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 58, DOUBLE_PACK, add, 0,
    PUSH, print, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 64, DOUBLE_PACK, add, 0,
    PUSH, print, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 60, DOUBLE_PACK, add, 0,
    PUSH, print, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 71, DOUBLE_PACK, add, 0,
    PUSH, print, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 125, DOUBLE_PACK, add, 0,
    PUSH, print, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 123, DOUBLE_PACK, add, 0,
    PUSH, print, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 33, DOUBLE_PACK, add, 0,
    PUSH, input, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 73, DOUBLE_PACK, add, 0,
    PUSH, input, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 54, DOUBLE_PACK, add, 0,
    PUSH, ext, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 84, DOUBLE_PACK, add, 0,
    PUSH, ext, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 97, DOUBLE_PACK, add, 0,
    PUSH, ext, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 118, DOUBLE_PACK, add, 0,
    PUSH, ext, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 89, DOUBLE_PACK, add, 0,
    PUSH, sum, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 122, DOUBLE_PACK, add, 0,
    PUSH, "YAY, You win!", _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 124, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 1, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 2, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 3, DOUBLE_PACK, add, 0,
    PUSH, 1337, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 4, DOUBLE_PACK, add, 0,
    PUSH, JNE, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 5, DOUBLE_PACK, add, 0,
    PUSH, 2, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 6, DOUBLE_PACK, add, 0,
    PUSH, COPY, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 7, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 9, DOUBLE_PACK, add, 0,
    PUSH, xor_36, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 10, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 11, DOUBLE_PACK, add, 0,
    PUSH, xor_36, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 12, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 13, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 14, DOUBLE_PACK, add, 0,
    PUSH, 7, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 15, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 16, DOUBLE_PACK, add, 0,
    PUSH, dmagic, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 17, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 18, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 19, DOUBLE_PACK, add, 0,
    PUSH, 17, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 20, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 21, DOUBLE_PACK, add, 0,
    PUSH, 134, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 22, DOUBLE_PACK, add, 0,
    PUSH, JNE, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 8, DOUBLE_PACK, add, 0,
    PUSH, "H3w1", _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 23, DOUBLE_PACK, add, 0,
    PUSH, 2, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 24, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 25, DOUBLE_PACK, add, 0,
    PUSH, 0xbeef, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 26, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 27, DOUBLE_PACK, add, 0,
    PUSH, -0x1337, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 28, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 29, DOUBLE_PACK, add, 0,
    PUSH, -0b1010101110110001, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 30, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 32, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 34, DOUBLE_PACK, add, 0,
    PUSH, JNE, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 35, DOUBLE_PACK, add, 0,
    PUSH, 2, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 36, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 37, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 38, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 39, DOUBLE_PACK, add, 0,
    PUSH, add, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 40, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 41, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 42, DOUBLE_PACK, add, 0,
    PUSH, add, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 43, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 44, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 45, DOUBLE_PACK, add, 0,
    PUSH, add, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 46, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 56, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 57, DOUBLE_PACK, add, 0,
    PUSH, "Yea, exactly:", _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 47, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 48, DOUBLE_PACK, add, 0,
    PUSH, dmagic, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 49, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 63, DOUBLE_PACK, add, 0,
    PUSH, 'sAHH\x04@KJA\t', _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 50, DOUBLE_PACK, add, 0,
    PUSH, JNE, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 51, DOUBLE_PACK, add, 0,
    PUSH, 4, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 52, DOUBLE_PACK, add, 0,
    PUSH, JMP_PLUS, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 53, DOUBLE_PACK, add, 0,
    PUSH, 4, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 55, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 59, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 61, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 69, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 70, DOUBLE_PACK, add, 0,
    PUSH, "Okay, the last one check! ^^", _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 66, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 67, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 68, DOUBLE_PACK, add, 0,
    PUSH, "Print your last seven symbols:\n", _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 62, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 65, DOUBLE_PACK, add, 0,
    PUSH, xor_36, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 72, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 74, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 75, DOUBLE_PACK, add, 0,
    PUSH, COPY, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 76, DOUBLE_PACK, add, 0,
    PUSH, sum_chars, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 77, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 78, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 79, DOUBLE_PACK, add, 0,
    PUSH, 512, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 80, DOUBLE_PACK, add, 0,
    PUSH, JNE, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 81, DOUBLE_PACK, add, 0,
    PUSH, 4, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 82, DOUBLE_PACK, add, 0,
    PUSH, JMP_PLUS, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 83, DOUBLE_PACK, add, 0,
    PUSH, 4, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 85, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 86, DOUBLE_PACK, add, 0,
    PUSH, beca, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 87, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 88, DOUBLE_PACK, add, 0,
    PUSH, COPY, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 109, DOUBLE_PACK, add, 0,
    PUSH, 27, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 90, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 104, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 105, DOUBLE_PACK, add, 0,
    PUSH, 0x4f, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 91, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 100, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 101, DOUBLE_PACK, add, 0,
    PUSH, 132, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 92, DOUBLE_PACK, add, 0,
    PUSH, 360, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 93, DOUBLE_PACK, add, 0,
    PUSH, JNE, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 94, DOUBLE_PACK, add, 0,
    PUSH, 4, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 95, DOUBLE_PACK, add, 0,
    PUSH, JMP_PLUS, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 96, DOUBLE_PACK, add, 0,
    PUSH, 4, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 102, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 107, DOUBLE_PACK, add, 0,
    PUSH, 0x61, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 103, DOUBLE_PACK, add, 0,
    PUSH, 25, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 98, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 99, DOUBLE_PACK, add, 0,
    PUSH, UNPACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 108, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 110, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 111, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 112, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 113, DOUBLE_PACK, add, 0,
    PUSH, DOUBLE_PACK, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 114, DOUBLE_PACK, add, 0,
    PUSH, JNE, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 106, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 115, DOUBLE_PACK, add, 0,
    PUSH, 4, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 116, DOUBLE_PACK, add, 0,
    PUSH, JMP_PLUS, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 117, DOUBLE_PACK, add, 0,
    PUSH, 3, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 119, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 121, DOUBLE_PACK, add, 0,
    PUSH, PUSH, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 126, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 127, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 128, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 129, DOUBLE_PACK, add, 0,
    PUSH, 0, _rerere_,
    PUSH_PTR, PUSH, -12, DOUBLE_PACK, sub, 0, PUSH, 120, DOUBLE_PACK, add, 0,
    PUSH, "Now you can listen to our addly music!", _rerere_,

    # нужно записать на позицию после _jump_ 0. В рамках этой виртуальной машины это очень neprosto
    # параметр 1. Что помещаем. А помещаем мы -(pos_jump+1)
    PUSH, 2,
    # параметр 2. Куда помещаем. Должен быть pos(_jump_) + 1 ==
    # _push_pointer_ + delta(_push_pointer_, _jump_) + 1 == _push_pointer_ + const
    PUSH_PTR,
    PUSH, -6,
    DOUBLE_PACK,
    sub, 0,
    _rerere_,
    # вауля! теперь у нас есть наш 0. Сколько инструкций? 7. Длина 11. position-independent code,
    # может работать из любого места.
    JMP_PLUS,
    0,
    0,
    0,
]

memory = inst_memory
data = data_memory
pointer = 0
while 1:
    if memory[pointer] == 0:
        p('EXIT')
        print("STOP VM")
        break
    elif memory[pointer] is JMP_PLUS:
        addr = memory[pointer+1]
        p(f'JMP_PLUS {addr}')
        pointer += addr
    elif memory[pointer] is JMP:
        addr = memory[pointer+1] - 1
        p(f'JMP {addr}')
        pointer = addr
    elif memory[pointer] is DOUBLE_PACK:
        p('POP; POP; PACK')
        p0, p1 = data.pop(), data.pop()
        data.append([*p0, *p1])
        pointer += 1
    elif memory[pointer] is JNE:
        p0, p1 = data.pop(), data.pop()
        pointer += 1
        jp = memory[pointer]
        p(f'CMP {p0} == {p1}; JNE {jp-1}')
        if p0 == p1:
            pointer += 1
        else:
            pointer += jp-1
    elif memory[pointer] is _rerere_:
        f0, o0 = data.pop()[0], data.pop()[0]
        memory[pointer+o0] = f0
        pointer += 1
    elif memory[pointer] is PACK: # [3] -> [[3]]
        f0 = data.pop()
        p(f'PACK # {f0} => [{f0}]')
        data.append([f0])
        pointer += 1
    elif memory[pointer] is UNPACK: # [[3]] -> [3]
        f0 = data.pop()
        f0 = f0[0]
        p(f'UNPACK # [{f0}] => {f0}')
        data.append(f0)
        pointer += 1
    elif memory[pointer] is COPY: # copy element on stack # pop ; push; push
        p0 = data.pop()
        p(f"POP {p0}; PUSH ; PUSH")
        data.append(p0)
        data.append(p0)
        pointer += 1
    elif memory[pointer] is PUSH:
        pointer += 1
        p0 = memory[pointer]
        data.append([p0])
        p(f'PUSH {[p0]}')
        pointer += 1
    elif memory[pointer] is PUSH_PTR:
        pointer += 1
        p(f'PUSH PTR {[pointer]}')
        data.append([pointer])
    else:
        fcall = []
        while memory[pointer] != 0:
            fcall.append(memory[pointer])
            pointer += 1

        param = data.pop()
        st = str(param)[1:-1]
        for fun in fcall[::-1]:
            st = f"{fun.__name__}({st})"
            param = [fun(*param)]
        p("PUSH "+st)
        if param[0] is not None:
            data.append(param)
        pointer += 1

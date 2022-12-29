import os


def make_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


def Base36(code):
    Base36_code = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    length = len(code)

    Base10 = 0

    for i in range(length):
        num = 0
        for b in Base36_code:
            if b == code[i].upper():
                Base10 += (num * (36 ** (length - i - 1)))
            num += 1
    return Base10


def waiting_time():
    return "잠시 기다려주세요"

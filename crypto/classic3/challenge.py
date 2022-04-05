import string
from secret import FLAG, KEY

flag = FLAG
key = KEY

possible_chars = string.ascii_letters + string.digits
n = len(possible_chars)
enc = ''

for c in flag :
    if c in possible_chars :
        i =  possible_chars.index(c)
        enc += possible_chars[(i + key) % n]
    else :
        enc += c

print(enc)
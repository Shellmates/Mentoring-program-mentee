import string
from secret import FLAG

flag = FLAG
key = "vigenere"

# I decided to use this alphabet for the vigenere cipher
alphabet = string.ascii_letters + string.digits + '}{_'
n = len(alphabet)
enc = ''

# Here is the vigenere cipher
for ind in range(len(flag)) :
    c = flag[ind]
    k = key[ind % len(key)]
    if c in alphabet :
        i = alphabet.index(c)
        j = alphabet.index(k)
        enc += alphabet[(i + j) % n]
    else :
        enc += c

print(enc)
import string

enc = "NpkpyqrxzAe5mL5Tlh4sHdumyVad7whdmVf4APzRlhzSapo"
key = "vigenere"

alphabet = string.ascii_letters + string.digits + '}{_'
n = len(alphabet)
flag = ''

for ind in range(len(enc)) :
    c = enc[ind]
    k = key[ind % len(key)]
    if c in alphabet :
        i = alphabet.index(c)
        j = alphabet.index(k)
        flag += alphabet[(i - j) % n]
    else :
        flag += c

print(flag)

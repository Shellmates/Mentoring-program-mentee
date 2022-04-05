import string

enc = "JyvCCDrKvJ{s8LKVWhItk_3rf_tFDk_yl4uP}"
possible_chars = string.ascii_letters + string.digits
n = len(possible_chars)

for key in range(len(possible_chars)):
    flag = ''
    for c in enc :
        if c in possible_chars :
            i =  possible_chars.index(c)
            flag += possible_chars[(i - key) % n]
        else :
            flag += c
    if 'shellmates' in flag :
        print(flag)
        exit()

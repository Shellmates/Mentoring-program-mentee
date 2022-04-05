import string

enc = "pnrfne vf fnzr nf ebg13, jryy urer vf lbhe synt furyyzngrf{v_ubcr_lbh_xabj_ubj_pnrfne_jbexf_abj}"
alphabet = string.ascii_lowercase
n = 26
key = 13

flag = ''
for c in enc :
    if c in alphabet :
        i =  alphabet.index(c)
        flag += alphabet[(i - key) % n]
    else :
        flag += c

print(flag)

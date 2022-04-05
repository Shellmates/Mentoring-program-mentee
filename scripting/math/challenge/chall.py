#!/usr/bin/python3

from sys import exit
import random
from time import time

RANGE = 100000000

FLAG = "shellmates{W3LL_I_H0P3_Y0U_did_17_W17|-|_PYTH0N}"

for i in range(1,101):
	op1, op2 = random.randrange(RANGE*i), random.randrange(RANGE*i)
	print(f"Operation : {op1}+{op2}")
	start = time()
	res = input("Result --> ")
	duration = time()-start
	
	if not res.isdigit() : 
		print("Answers should be numerical")
		exit()
	elif duration > 2 : 
		print("BRUUUH, that was too slow")
		exit()
	else : 
		if op1+op2 != int(res) :
			print("WRONG!!!")
			exit()

print(f"Congrats, Here is your flag : {FLAG}")
exit()
#!/usr/local/bin/python3
from pwn import *
x=[]
intList = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304823, 962880562, 895706419]
for each in intList:
    a=p32(each, endian='big')
    a=str(a)
    a=a[2:-1]
    x.append(a)
print(''.join(x))

#!/usr/local/bin/python3
binStr = "01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010"
binList = binStr.split(" ")
flag = ""

for each in binList:
    binInt = int(each, 2)
    secChar = chr(binInt)
    flag+=secChar

print(flag)

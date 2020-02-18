#!/usr/local/bin/python3
'''
what does
asm3(0xaeed09cb,0xb7acde91,0xb7facecd)
return?
asm3:
	<+0>:   push   ebp
	<+1>:   mov    ebp,esp

	<+3>:   xor    eax,eax
	<+5>:   mov    ah,BYTE PTR [ebp+0xb]
	<+8>:   shl    ax,0x10
	<+12>:  sub    al,BYTE PTR [ebp+0xe]
	<+15>:  add    ah,BYTE PTR [ebp+0xd]
	<+18>:  xor    ax,WORD PTR [ebp+0x12]

	<+22>:  nop

	<+23>:  pop    ebp

	<+24>:  ret
asm3(0xaeed09cb,0xb7acde91,0xb7facecd)
		arg1		arg2		arg3

[....][....][....][....] [....][....][....][....] EAX: full 32bits val
                         [....][....][....][....] AX: lower 16bits
                         [....][....]             AH: higher 8bits
                                     [....][....] AL: lower 8bits
'''
from struct import pack, unpack

def encodeE (input):
    return pack ('<I', input) # => little endian
def decodeE (input):
    return unpack('<H', input)[0] #H: unsigned int 16bits. [0]:tuple

#first, load ebp and eip on the stack, then we load the arguments in
#also make it bytearray to we can access the byte locations easily
stack = bytearray(encodeE(0) + encodeE(0) + encodeE(0xaeed09cb) + encodeE(0xb7acde91) + encodeE(0xb7facecd))

#<asm+5>
ax = stack[11] << 8
#<asm+8>
ax = ((ax & 0xffff) << 0x10) & 0xffff #eax & 0xffff: bottom 16bits of eax
#<asm+12>
al = ((ax & 0xff) - stack[0xe]) & 0xff
ax = (ax & 0xff00) | al
#<asm+15
ah = (((ax >> 8) & 0xff) + stack[0xd]) & 0xff
ax = (ax & 0x00ff) | (ah << 8)
#<asm+18>
ax ^= decodeE(stack[0x12:0x14])
print("0x%.4x" % ax)

encflag=[ 0xac, 0xf3, 0x0c, 0x25, 0xa3, 0x10, 0xb7, 0x25, 0x16, 0xc6, 0xb7, 0xbc, 0x07, 0x25, 0x02, 0xd5, 0xc6, 0x11, 0x07, 0xc5]

flag = list(' '*20)

for i in range(20):
	flag[i] = int(encflag[i] / -5)

print(flag)

for i in flag:
	print(chr(i), end='')

first_key = b'\x53\x4b\x52\x7b\x58\x6f\x52\x46'
first_key = list(first_key.decode())

# first_key: SKR{XoRF
print("first_key: ",first_key)

enc = b'\x63\x39\x1e\x4a\x3e\x5c\x73\x3b'
enc = enc.decode()
enc = list(enc)

second_key = list(' '*8)

for i in range(8):
	second_key[i] = chr(ord(first_key[i])^ord(enc[i]))

print("first_key: ",first_key)
print("second_key: ",second_key)

flag = first_key + second_key

print(''.join(flag))

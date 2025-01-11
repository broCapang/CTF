flag = list("EZPZ_XXXXXXXXXXXXXXXX")
for i in range(len(flag)):
    for c in range(256):
        flag[i] = chr(c)
        if i > 0:
            flag[i] = chr(ord(flag[i]) ^ ord(flag[i-1]))
        flag[i] = chr(ord(flag[i]) ^ (ord(flag[i]) >> 4))
        flag[i] = chr(ord(flag[i]) ^ (ord(flag[i]) >> 3))
        flag[i] = chr(ord(flag[i]) ^ (ord(flag[i]) >> 2))
        flag[i] = chr(ord(flag[i]) ^ (ord(flag[i]) >> 1))
    print(flag[i])

# Print the bytes of the final result
result = ''.join(flag)
print([ord(c) for c in result])

for i in range(len(flag)):
    for c in range(256):
        flag[i] = chr(c)
        flag[i] = chr(ord(flag[i]) ^ (ord(flag[i]) >> 1))
        flag[i] = chr(ord(flag[i]) ^ (ord(flag[i]) >> 2))
        flag[i] = chr(ord(flag[i]) ^ (ord(flag[i]) >> 3))
        flag[i] = chr(ord(flag[i]) ^ (ord(flag[i]) >> 3))

        if i > 0:
            flag[i] = chr(ord(flag[i]) ^ ord(flag[i-1]))
    print(flag[i])


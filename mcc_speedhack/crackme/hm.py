flag = [ 0x76, 0x31, 0x49, 0x1e, 0x71, 0x1f, 0x40, 0x53, 0x24, 0x7b, 0x18, 0x34, 0x75, 0x35, 0x6b, 0x15, 0x3c, 0x7b, 0x7c, 0x1d, 0x32 ]

for i in range(len(flag)):

    for c in range(256,0,-1):  # Loop through all possible byte values (0 to 255)
       
       flag[i] = c
       if (i > 0):
           flag[i] ^= flag[i-1];
       flag[i]^= flag[i] <<1
       flag[i] ^= flag[i] << 2
       flag[i]^= flag[i] << 3
       flag[i] ^= flag[i] << 4
       flag[i]&=0xFF
print(''.join(flag))

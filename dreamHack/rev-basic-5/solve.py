

# enc_flag[i] = z[i] + z[i+1]

# when i = n

# enc_flag[n] = z[n] 

# flag[n] = z[n]

# enc_flag[n-1] - z[n]= z[n-1] 
enc_flag = [ 0xad, 0xd8, 0xcb, 0xcb, 0x9d, 0x97, 0xcb, 0xc4, 0x92, 0xa1, 0xd2, 0xd7, 0xd2, 0xd6, 0xa8, 0xa5, 0xdc, 0xc7, 0xad, 0xa3, 0xa1, 0x98, 0x4c ]
flag = ' '*len(enc_flag)
flag = list(flag)

flag[len(enc_flag)-1] = enc_flag[len(enc_flag)-1]

for i in range(len(enc_flag)-1,0,-1):
	flag[i-1] = enc_flag[i-1] - flag[i]

print(''.join(chr(i) for i in flag))


'''
All_l1fe_3nds_w1th_NULL
'''

flag = list(' '*30)


encflag = [ 0x52, 0xdf, 0xb3, 0x60, 0xf1, 0x8b, 0x1c, 0xb5, 0x57, 0xd1, 0x9f, 0x38, 0x4b, 0x29, 0xd9, 0x26, 0x7f, 0xc9, 0xa3, 0xe9, 0x53, 0x18, 0x4f, 0xb8, 0x6a, 0xcb, 0x87, 0x58, 0x5b, 0x39, 0x1e ]


def decode_enc_flag(enc_flag):
    input = [0] * len(enc_flag)
    
    for i in range(len(enc_flag)):
        if i > 30:
            return 1
        
        k = i & 7
        encoded_value = enc_flag[i]
        
        temp = encoded_value ^ i
        input[i] = (temp >> k) | (temp << (8 - k))
        
        input[i] &= 0xFF
    
    return input

decoded_input = decode_enc_flag(encflag)

for i in decoded_input:
	print(chr(i), end='')




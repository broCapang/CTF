def xor_byte(data, key):
    length = len(key)
    for i in range(0x20):
        data[i] ^= key[i % length]

def increase_I(data, value):
    for i in range(0x20):
        data[i] = (data[i] + value) 

def decrease_I(data, value):
    for i in range(0x20):
        data[i] = (data[i] - value) 

def invert_operations(data, first_bytes, second_bytes, third_bytes):
    xor_byte(data, third_bytes)
    increase_I(data, -0xF3)  # Equivalent to increase_I with positive value
    decrease_I(data, -0x4D)  # Equivalent to decrease_I with positive value
    xor_byte(data, second_bytes)
    decrease_I(data, -0x5A)  # Equivalent to decrease_I with positive value
    increase_I(data, -0x1F)  # Equivalent to increase_I with positive value
    xor_byte(data, first_bytes)

enc_flag = [ 0xf8, 0xe0, 0xe6, 0x9e, 0x7f, 0x32, 0x68, 0x31, 0x05, 0xdc, 0xa1, 0xaa, 0xaa, 0x09, 0xb3, 0xd8, 0x41, 0xf0, 0x36, 0x8c, 0xce, 0xc7, 0xac, 0x66, 0x91, 0x4c, 0x32, 0xff, 0x05, 0xe0, 0xd9, 0x91]

firstBytes = [ 0xde, 0xad, 0xbe, 0xef]

secondBytes = [ 0xef, 0xbe, 0xad, 0xde]

thirdBytes = [ 0x11, 0x33, 0x55, 0x77, 0x99, 0xbb, 0xdd]

print('Length: ',len(enc_flag))

"""
enc_flag = xor_byte(enc_flag,firstBytes)
enc_flag = increase_I(enc_flag, 0x1f)  # Providing num as an integer
enc_flag = subtract_I(enc_flag, 0x5a)  # Providing num as an integer
enc_flag = xor_byte(enc_flag, secondBytes)
enc_flag = subtract_I(enc_flag, 0x4d)  # Providing num as an integer
enc_flag = increase_I(enc_flag, 0xf3)  # Providing num as an integer
enc_flag =xor_byte(enc_flag, thirdBytes)
"""

# Call the function to invert the operations
invert_operations(enc_flag, firstBytes, secondBytes, thirdBytes)


print(enc_flag)
flag = [chr(value) for value in enc_flag]
print(flag)


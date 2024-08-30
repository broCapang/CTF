# Hex values from the code
local_38 = 0x3935643530356435.to_bytes(8, byteorder='big')
local_30 = 0x6532353530326131.to_bytes(8, byteorder='big')
local_28 = 0x3233643339323734.to_bytes(8, byteorder='big')
local_20 = 0x3365336335.to_bytes(5, byteorder='big')
uStack_1b = 0x393531.to_bytes(3, byteorder='big')
uStack_18 = 0x63313932.to_bytes(4, byteorder='big')

# Concatenate the hex values to form the original encoded message
encoded = local_38 + local_30 + local_28 + local_20 + uStack_1b + uStack_18

# XOR key
local_46 = 0x7361616d616e.to_bytes(6, byteorder='big')
uStack_40 = 0x6c61.to_bytes(2, byteorder='big')
uStack_3e = 0x6861626173.to_bytes(5, byteorder='big')

# Concatenate the XOR key parts
xor_key = (local_46 + uStack_40 + uStack_3e)

# Now reverse the XOR operation
flag = bytes([b ^ xor_key[i % len(xor_key)] for i, b in enumerate(encoded)])

# Convert the flag from bytes to string
print(flag.decode())


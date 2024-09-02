def reverse_local_b8(local_b8):
    input_array = []
    for i in range(32):  # Assuming local_b8 has 32 elements
        if i % 2 == 0:
            original_value = local_b8[i]  # multiplier was 1
        else:
            original_value = local_b8[i] // 2  # multiplier was 2

        # Reverse the XOR operation
        input_value = original_value ^ i
        input_array.append(input_value)
    
    return input_array

local_b8 = [
    0x43, 0xa4, 0x41, 0xae, 0x42, 0xfc, 0x73, 0xb0, 0x6f, 0x72, 0x5e, 0xa8,
    0x65, 0xf2, 0x51, 0xce, 0x20, 0xbc, 0x60, 0xa4, 0x6d, 0x46, 0x21, 0x40,
    0x20, 0x5a, 0x2c, 0x52, 0x2d, 0x5e, 0x2d, 0xc4
]

# Reverse to find the input array
input_array = reverse_local_b8(local_b8)
input_array_hex = [hex(val) for val in input_array]
print(''.join(input_array_hex))

# Define the key used for encoding
key = "COVID-19"

# Open the encoded file in binary read mode
encoded_file_path = "flag.kolona"
decoded_file_path = "decoded_flag.jpg"

with open(encoded_file_path, "rb") as kolona, open(decoded_file_path, "wb") as decoded_flag:
    encoded_content = kolona.read()
    decoded_content = bytearray()

    # Decode each byte using XOR with the key
    for i, byte in enumerate(encoded_content):
        decoded_byte = byte ^ ord(key[i % len(key)])
        decoded_content.append(decoded_byte)

    # Write the decoded content to the new file
    decoded_flag.write(decoded_content)


'''
SKR{V1rus_1s_3verywhere_pl3453_st4y_4t_H0me}
'''
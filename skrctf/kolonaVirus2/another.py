key = "SARS-CoV-2"

def decrypt_kolona(encrypted_data, key, random_num):
    decrypted_data = bytearray()
    key_len = len(key)
    for i, c in enumerate(encrypted_data):
        decrypted_byte = (c - ord(key[i % key_len]) - random_num) % 256
        decrypted_data.append(decrypted_byte)
    return decrypted_data

with open("flag.kolona", "rb") as kolona_file:
    encrypted_data = kolona_file.read()

for random_num in range(1, 6667):
    decrypted_data = decrypt_kolona(encrypted_data, key, random_num)
    if decrypted_data[:8] == b'\x89PNG\r\n\x1a\n':   ## valid PNG file signature (first 8 bytes in hex: 89 50 4E 47 0D 0A 1A 0A) ASCII representation
        with open("decrypted_flag.png", "wb") as output_file:
            output_file.write(decrypted_data)
        print(f"Successfully decrypted with random_num = {random_num}")
        break

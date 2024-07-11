# Read the files in binary mode
with open('MT568643', 'rb') as f:
    kolona_genome = f.read()

with open('original_virus', 'rb') as f:
    original_virus = f.read()

kolona_rna = [9728,
 9150,
 9459,
 25263,
 1634,
 27368,
 11779,
 19149,
 9629,
 2721]
kolona_rna2 = [5676,
 10615,
 13415,
 16286,
 17093,
 13804,
 26647,
 26800,
 4547,
 13208]

# Initialize the evolve_virus as a bytearray
evolve_virus = bytearray()

# Iterate through the original virus and evolve it
for i in range(len(original_virus)):
    evolved_byte = (original_virus[i] - kolona_genome[kolona_rna[i % 10]] - kolona_genome[kolona_rna2[i % 10]]) % 256
    evolve_virus.append(evolved_byte)

# Convert the evolved virus to a string for execution
evolve_virus_str = evolve_virus.decode('latin1')  # Using 'latin1' to avoid decode errors

# Execute the evolved virus
print(evolve_virus_str)

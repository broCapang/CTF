from z3 import *

# Given encrypted flag (hex string converted to bytes)
enc_flag = b"7631491e711f4053247b183475356b153c7b7c1d32"

# Define the solver
solver = Solver()

# Create a list of BitVec variables for each character in the flag (8-bit per character)
flag = [BitVec(f"flag_{i}", 8) for i in range(len(enc_flag))]

# Add constraints to match the encrypted values (ensure flag[i] matches the encrypted byte)
for i in range(len(enc_flag)):
    solver.add(flag[i] == enc_flag[i])

# Now, apply the reverse XOR logic:
for i in range(len(enc_flag) - 1, 0, -1):  # Start from the last character
    # Reverse XOR with the previous character
    solver.add(flag[i] == flag[i] ^ flag[i-1])

    # Reverse the bit shifts
    solver.add(flag[i] == flag[i] ^ (flag[i] >> 1))
    solver.add(flag[i] == flag[i] ^ (flag[i] >> 2))
    solver.add(flag[i] == flag[i] ^ (flag[i] >> 3))
    solver.add(flag[i] == flag[i] ^ (flag[i] >> 4))

# Reverse the XOR operation for the first character (it has no previous character to XOR with)
solver.add(flag[0] == flag[0] ^ flag[0])  # This just nullifies itself.

# Check if there is a solution
if solver.check() == sat:
    model = solver.model()
    result = ''.join([chr(model[flag[i]].as_long()) for i in range(len(flag))])
    print("Recovered flag:", result)
else:
    print("No solution found")


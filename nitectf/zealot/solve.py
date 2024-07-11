from z3 import *

# Create a solver instance
s = Solver()

# Create an array of 42 byte variables (since the highest index used is 41)
a1 = [BitVec(f'a1[{i}]', 8) for i in range(42)]

# Assigning values and conditions
# Direct conditions
s.add(a1[5] == 84)
s.add(a1[6] == 70)
s.add(a1[8] == 103)
s.add(a1[21] == 116)
s.add(a1[17] == 104)
s.add(a1[12] == 95)
s.add(a1[1] == 105)

# Complex conditions that need calculations or logical operations
s.add(a1[0] == a1[40])
s.add(a1[1] == (a1[37] ^ 0x1D))
s.add(a1[3] == a1[18])
s.add(a1[18] == a1[32])
s.add(a1[37] != 32)
s.add(a1[7] + 2 == a1[41])
s.add(32 * a1[8] == 3296)
s.add(a1[9] == a1[10])
s.add(a1[14] == a1[29])
s.add(a1[29] == a1[39])
s.add(a1[16] == ((((a1[12] + 2051495600) & 0x4894482C | 0x4280202) ^ 0x4C2C4251) & 0xFF))
s.add(a1[0] == 110)
s.add(a1[31] ^ a1[41] == ((a1[14] ^ 0x8E56) ^ 0x6D))
s.add(a1[23] == ((((a1[12] - 903645652) & 0x62486926 | 0x4020040) ^ 0x4602601D) & 0xFF))
s.add(a1[2] == 116)
s.add(a1[27] == ((((a1[12] + 802870624) & 0xC0A28043 | 0x395D4B28) ^ 0x39DFCB74) & 0xFF))
s.add(a1[31] == ((((a1[12] + 1050330464) & 0xDA04A63F | 0x995980) ^ 0x1A99DDE0) & 0xFF))
s.add(a1[24] ^ 0x66 == (a1[26] & 0x400001 | 0x64))
s.add((a1[24] ^ 0x62) & 1 | 0x64 == a1[33])
s.add(((((a1[28] << 25) ^ 0x60000000) & 0x200610 | 0x63) & 0xFF) == a1[35])
s.add(a1[3] == 101)
s.add(a1[28] == 102)
s.add(a1[6] + 34 == a1[17])
s.add(a1[41] == 125)
s.add(a1[20] == ((a1[1] + a1[3]) & 0x8450 ^ 0x40 | 0x6C) & 0xFF)
s.add(a1[36] == a1[19])
s.add(a1[19] == a1[6] + 27)
s.add(a1[34] != -563555251)
s.add(a1[25] == (((a1[4] >> 3) & 0x120D ^ 0x69) & 0xFF))
s.add(a1[21] != a1[37])
s.add(a1[20] ^ 0x4E | 0x50 == a1[15])
s.add(a1[20] ^ 0x4E | 0x50 == a1[30])
s.add(a1[11] == a1[22] - 4)
s.add(a1[22] == ((a1[9] ^ a1[12]) & 0xB00B ^ 0x68) & 0xFF)
s.add(a1[30] == a1[15])
s.add(a1[24] == ((((a1[5] - 456630272) & 0x9594815B | 0x4A6B0680) ^ 0xCEEB06B2) & 0xFF))
s.add(a1[9] == 111)
s.add(a1[4] == 67)
s.add(a1[38] == (~(a1[13]) & a1[20] ^ 9 | 0x68) & 0xFF)
s.add((a1[13] ^ 0x62) == (a1[20] & 0x4696 & 0xFF))

# Check if the constraints can be satisfied
if s.check() == sat:
    m = s.model()
    solution = [m.evaluate(a1[i]).as_long() for i in range(42)]
    print("Solution:", solution)
else:
    print("No solution found")

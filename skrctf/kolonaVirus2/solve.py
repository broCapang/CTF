import random
flag = open("flag.png","r")
kolona = open("flag.kolona","w+")
key = "SARS-CoV-2"
# Prevent Reverse Engineering!
random_num = random.randint(1,6666)

for i,c in enumerate(flag.read()):
	kolona.write(chr((ord(c) + ord(key[i % len(key)]) + random_num) % 256))
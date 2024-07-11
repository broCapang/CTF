# a = lambda a, b: a + b
# b = lambda b, c: a(b, -c)
# c = lambda c: b(c, -c)

# a(p[0], p[1]) == c(52) 
# p[0] + p[1] = 104

# b(p[1], p[0]) == -2
# p[1] - p[0] = -2

p = ' '*8

p = list(p)

p[0]  = chr(53)
p[1] = chr(51)



# a(p[2], p[3]) - b(p[3], p[2]) == a(int(chr(p[0]) + chr(p[1])), 45)
# c(p[2]) + c(p[3]) == b(-1141, -1337)

p[2] = chr(49)
p[3] = chr(49)

# a(c(p[4]), c(p[5])) == c(108) 
# b(c(p[5]), c(p[4])) == -12

p[4] = chr(57)


p[5] = chr(51) 


# b(a(p[6], p[7]), b(p[6], p[7])) == 108
# b(c(b(p[7], p[6])), a(p[7], p[6])) == -111

p[7] = chr(54)

p[6] = chr(55)

print(''.join(p))
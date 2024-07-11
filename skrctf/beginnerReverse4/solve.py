#/usr/bin/env python3

part1 = 'Spr3ue45'

part2 = '5PrcS3u'


password = " " *15

password = list(password)


j = 0
for i in range(0, 15, 2):
	password[i] = part1[j]
	print(f'i:',i, end=' ')
	print(f'j:',j)
	j += 1 

j=0
for i in range(15-2, 0, -2):
	password[i] = part2[j]
	print(f'i:',i, end=' ')
	print(f'j:',j)
	j += 1 


print(len(password))
print("".join(password))

'''
for (int i = 0, j = 0; i < length; i+=2,j++){
	if(pass[i] != part1[j]){
		return 0;
	}
}	

for (int i = length-2, j = 0; i > 0; i-=2,j++){
	if(pass[i] != part2[j]){
		return 0;
	}
}
'''
#!/usr/bin/env python3


length = 17

'''
	if(pass[0] != 'R'){
		return 0;
	}
	if(pass[1] - pass[0] != -31 || pass[1] != pass[3]){
		return 0;
	}
	if(pass[4] != tolower(pass[0]) || pass[2] - pass[4] != 4){
		return 0;
	}
	if(pass[5] != '5' || pass[5] - pass[6] != 4){
		return 0;
	}
	if(pass[7] != pass[0] + 28 || pass[2] - pass[8] != 47){
		return 0;
	}
	if(pass[9] != '_' || pass[12] != pass[9] || strncmp(pass+13,"Fun!",4) != 0 || strncmp(pass+10,"1s",2) != 0){
		return 0;
	}
'''

password = ' '*17

password = list(password)
password[0] = 'R'

password[1] = chr(-31 + ord(password[0]))
password[3] = password[1]
password[4] = password[0].lower()
password[2] =chr( 4 + ord(password[4]))
 
password[5] = '5'
password[6] = chr( ord(password[5]) - 4) 
password[7] = chr(ord(password[0]) + 28)
password[8] = chr(ord(password[2]) - 47) 
password[9] = '_'
password[10] = '1'
password[11] = 's'
password[12] = password[9] 
password[13]= "F"
password[14] = "u"
password[15] = 'n'
password[16] = '!'


print(''.join(password))
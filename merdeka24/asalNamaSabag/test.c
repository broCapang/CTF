int main(){  
	int iVar1;
  int len;
  char local_46 [6];
  char local_38 [38];
  int i;
  
  local_38[0] = '5';
  local_38[1] = 'd';
  local_38[2] = '5';
  local_38[3] = '0';
  local_38[4] = '5';
  local_38[5] = 'd';
  local_38[6] = '5';
  local_38[7] = '9';
  local_38[8] = '1';
  local_38[9] = 'a';
  local_38[10] = '2';
  local_38[0xb] = '0';
  local_38[0xc] = '5';
  local_38[0xd] = '5';
  local_38[0xe] = '2';
  local_38[0xf] = 'e';
  local_38[0x10] = '4';
  local_38[0x11] = '7';
  local_38[0x12] = '2';
  local_38[0x13] = '9';
  local_38[0x14] = '3';
  local_38[0x15] = 'd';
  local_38[0x16] = '3';
  local_38[0x17] = '2';
  local_38[0x18] = '5';
  local_38[0x19] = 'c';
  local_38[0x1a] = '3';
  local_38[0x1b] = 'e';
  local_38[0x1c] = '3';
  local_38[0x1d] = '1';
  local_38[0x1e] = '5';
  local_38[0x1f] = '9';
  local_38[0x20] = '2';
  local_38[0x21] = '9';
  local_38[0x22] = '1';
  local_38[0x23] = 'c';
  local_38[0x24] = '\0';
  local_46[0] = 'n';
  local_46[1] = 'a';
  local_46[2] = 'm';
  local_46[3] = 'a';
  local_46[4] = 'a';
  local_46[5] = 's';
  len = strlen(local_46);
//  for (i = 0; i < 37; i = i + 1) {
  //  local_38[(int)i] = local_38[(int)i] ^ local_46[(int)i % (int)len];
//}
printf("flag: %s",local_38);
}

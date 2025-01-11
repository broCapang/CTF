#include <stdio.h>
#include <string.h>

int main() {
  char flag[] = "EZPZ_XXXXXXXXXXXXXXXX";
  int len = strlen(flag);

  for (int i = 0; i < len; i++) 
  {
    for (int c = 0; c < 256; c++) 
    {

	    flag[i] = c;
	    if (i > 0) flag[i] ^= flag[i-1];
	    flag[i] ^= flag[i] >> 4;
	    flag[i] ^= flag[i] >> 3;
	    flag[i] ^= flag[i] >> 2;
            flag[i] ^= flag[i] >> 1;
    }
    printf("%X\n",flag[i]);
  }
      for (int i = 0; flag[i] != '\0'; i++) {
        printf("%02X ", (unsigned char)flag[i]); // Convert to unsigned to avoid issues with signed char
    }
      printf("\n");
  return 0;
}

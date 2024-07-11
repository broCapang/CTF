#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  	char input [12];
	int a;

	printf("Which door would you like to open? ");
	scanf("%11s",input);
	getchar();

	a = atoi(input);
	printf("String value = %s, Int value = %x\n", input, a);
}
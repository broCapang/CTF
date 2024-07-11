#include <stdio.h>
#include <stdlib.h>

int main() {
	int input1;
	int input2;
	scanf("%d %d",&input1,&input2);

	printf("%d %d\n", input1,input2);
	if (((input1 == 0) || (input2 == 0)) || (input2 == 1)) {
    	puts("Nope! 1");
    	exit(1);
	}
	int divide = 0;

	if (input2 != 0) {
	  	divide = input1 / input2;
	  	printf("%d\n", divide);
	}
	if (divide != input1) {
	    puts("Nope! 2");
	    exit(1);
	}
	
	return 0;
}
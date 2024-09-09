#include <stdio.h>

int main(){
	FILE *filep;
	char buffer[1000];
	filep = fopen("/flag","r");
	if (filep == NULL){
		printf("can open");
		return 1;
	}
	while(fgets(buffer, sizeof(buffer), filep) != NULL) {
		printf("flag: %s",buffer);
	}
	fclose(filep);

	return 0;
}

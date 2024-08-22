#define BUFSIZE 100

long get_random() {
	return rand() % BUFSIZE;
}



long increment(long in) {
	return in + 1;
}

int main(int argc, char** argv){


	long ans;
	

	for(int i=0;i<10;i++){
		ans = get_random();
		ans = increment(ans);
		printf("Num: %d\n",ans);
	}

	return 0;

}

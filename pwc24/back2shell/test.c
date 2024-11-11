
int main(){

	char buf[] = "Helloworld!!! Welcome to my challenge!";
	puts(sizeof(buf)-1);
	puts(&buf[sizeof(buf)-1]);
	puts(&buf);
}

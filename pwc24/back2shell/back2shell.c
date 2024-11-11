#include <stdio.h>

void custom_write(char* buf) {
    read(0, buf, 0x40);
}

void init() {
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
}

int main() {
    char buf[] = "Helloworld!!! Welcome to my challenge!";
    init();
    printf("%s\n", buf);
    printf("%p\n", buf);
    custom_write(&buf[sizeof(buf)-1]);
    return 0;
}
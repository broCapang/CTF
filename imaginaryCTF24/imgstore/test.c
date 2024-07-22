int main(){
    int fd;
    int smtg;
    char *local_38;
    fd = open("/dev/urandom",0);
    read(fd,&smtg,4);
    close(fd);
    smtg &= 0xffff;
    printf("%d\n", smtg);
  	for (local_38 = "                  .----.   \n      .---------. | == |   \n      |.-\"\"\"\"\"-.| |----|   \n       ||       || | == |   \n      ||       || |----|   \n      |\'-.....-\'| |::::|   \n      `\"\")---(\"\"` |___.|   \n     /:::::::::::\\\" _  \"   \n    /:::=======:::\\`\\`\\   \n    `\"\"\"\"\"\"\"\"\"\"\"\"\"`  \'-\'   \n"; *local_38 != '\0'; local_38 = local_38 + 1) {

	    putchar((int)*local_38);
	}

    return 0;
}





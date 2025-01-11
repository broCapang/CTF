int main(){

	    int i = 1337;
    int j;
    i = i++ + ++i;
    j = i-- * i++;
    printf("i: %d, j: %d",i, j);
}

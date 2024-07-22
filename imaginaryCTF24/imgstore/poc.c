int main(){

  int iVar1;
  time_t tVar2;
  long in_FS_OFFSET;
  char *local_38;
  undefined *local_28 [3];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_28[0] = &DAT_00103320;
  local_28[1] = &DAT_00103326;
  tVar2 = time((time_t *)0x0);
  srand((uint)tVar2);
  for (local_38 = 
       "                  .----.   \n      .---------. | == |   \n      |.-\"\"\"\"\"-.| |----|   \n       ||       || | == |   \n      ||       || |----|   \n      |\'-.....-\'| |::::|   \n      `\"\")---(\"\"` |___.|   \n     /:::::::::::\\\" _  \"   \n    /:::=======:::\\`\\`\\   \n    `\"\"\"\"\"\"\"\"\"\"\"\"\"`  \'-\'   \n"
      ; *local_38 != '\0'; local_38 = local_38 + 1) {
    if (*local_38 == '\n') {
      putchar((int)*local_38);
    }
    else {
      iVar1 = FUN_001018c8(0,1);
      printf("%s%c\x1b[0m",local_28[iVar1],(ulong)(uint)(int)*local_38);
    }
  }
  
}
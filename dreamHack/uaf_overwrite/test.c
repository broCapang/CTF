#include <stdio.h>

// Define the Human struct
struct Human {
  char name[16];
  int weight;
  long age;
};

// Define the Robot struct
struct Robot {
  char name[16];
  int weight;
  void (*fptr)();
};

int main() {
    // Create instances of Human and Robot
    struct Human aHuman;
    struct Robot aRobot;

    // Output the size of the entire struct
    printf("Size of Human: %lu bytes\n", sizeof(struct Human));
    printf("Size of Robot: %lu bytes\n", sizeof(struct Robot));

    // Output the size of individual elements in the Human struct
    printf("Size of Human.name: %lu bytes\n", sizeof(aHuman.name));
    printf("Size of Human.weight: %lu bytes\n", sizeof(aHuman.weight));
    printf("Size of Human.age: %lu bytes\n", sizeof(aHuman.age));

    // Output the size of individual elements in the Robot struct
    printf("Size of Robot.name: %lu bytes\n", sizeof(aRobot.name));
    printf("Size of Robot.weight: %lu bytes\n", sizeof(aRobot.weight));
    printf("Size of Robot function pointer: %lu bytes\n", sizeof(aRobot.fptr));

    return 0;
}


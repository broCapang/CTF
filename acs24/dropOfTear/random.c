#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Characters of the flag prefix
    char prefix[] = "ACS{";

    // Convert the first 4 bytes to an integer
    int seed = 0;
    memcpy(&seed, prefix, sizeof(seed)); // Copies 4 bytes into the integer

    // Set the seed for srand
    srand(seed);

    // Example: Generate a random number to test
    printf("Random number: %d\n", rand());

    return 0;
}


#include <stdio.h>
#include <stdlib.h>

int main() {
    int input1, input2;
    int divide;

    // Define the range for input1 and input2
    int startRange = 1;
    int endRange = 1000000; // Example range, you can adjust it as needed

    printf("Finding valid (input1, input2) pairs where divide = input1 / input2 results in divide == input1\n");
    
    for (input1 = startRange; input1 <= endRange; input1++) {
        for (input2 = startRange; input2 <= endRange; input2++) {
            if (input2 == 1) {
                // Skip invalid values for input2
                continue;
            }

            divide = input1 / input2;

            if (divide == input1) {
                printf("Valid pair found: input1 = %d, input2 = %d\n", input1, input2);
            }
        }
    }

    printf("Finished searching for valid pairs.\n");
    return 0;
}


#include <stdio.h>
#include <string.h>

void reverse_flag(int* enc, int len) {
    for (int i = len - 1; i >= 0; i--) {
        // Reverse bitwise XOR transformations
        for (int shift = 1; shift <= 4; shift++) {
            enc[i] ^= enc[i] >> shift;
        }

        // Reverse XOR with enc[i-1] (if i > 0)
        if (i > 0) {
            enc[i] ^= enc[i-1];
        }
    }
}

int main() {
    // Using an array of int (32-bit) for the given hex values
    int enc[] = {0x763, 0x149, 0x1e7, 0x11f, 0x405, 0x324, 0x7b1, 0x834, 0x753, 0x56b, 0x153, 0xc7b, 0x7c1, 0xd32};
    int len = sizeof(enc) / sizeof(enc[0]);  // Correct way to calculate the length of the array

    reverse_flag(enc, len);

    // Print out the original flag values (in decimal for clarity)
    for (int i = 0; i < len; i++) {
        printf("%d ", enc[i]);  // Print each element as decimal
    }

    return 0;
}


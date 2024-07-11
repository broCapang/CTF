#include <stdio.h>

int main() {
    for (int x = -100; x <= 100; x++) {
        if (x == 0) continue; // Skip x = 0

        for (int y = -100; y <= 100; y++) {
            if (y == 0 || y == 1 ) continue; // Skip y = 0, 1, and -1

            int result = x / y;
            if (result == x) {
                printf("Found: x = %d, y = %d\n", x, y);
            }
        }
    }

    printf("No values of x and y found where x / y = x\n");
    return 0;
}

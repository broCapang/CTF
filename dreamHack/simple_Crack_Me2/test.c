#include <stdio.h>
#include <string.h>

void xor_byte(char* param_1, const char* param_2)
{
    int length;
    int i;

    length = strlen(param_2);
    for (i = 0; i < 0x20; i += 1) {
        param_1[i] = param_2[i % length] ^ param_1[i];
    }
}

void increase_I(char* param_1, int param_2)
{
    int i;

    for (i = 0; i < 0x20; i += 1) {
        param_1[i] = param_2 + param_1[i];
    }
}

void decrease_I(char* param_1, int param_2)
{
    int i;

    for (i = 0; i < 0x20; i += 1) {
        param_1[i] =  param_1[i]- param_2 ;
    }
}

int main() {
    char input[] = {0xf8, 0xe0, 0xe6, 0x9e, 0x7f, 0x32, 0x68, 0x31, 0x05, 0xdc, 0xa1, 0xaa, 0xaa, 0x09, 0xb3, 0xd8, 0x41, 0xf0, 0x36, 0x8c, 0xce, 0xc7, 0xac, 0x66, 0x91, 0x4c, 0x32, 0xff, 0x05, 0xe0, 0xd9, 0x91};
    const char first_bytes[] = { 0xde, 0xad, 0xbe, 0xef}; // Replace with actual string
    const char second_bytes[] = {0xef, 0xbe, 0xad, 0xde}; // Replace with actual string
    const char third_bytes[] =  {0x11, 0x33, 0x55, 0x77, 0x99, 0xbb, 0xdd}; // Replace with actual string
    printf("Input: ");
    for (int i = 0; i < strlen(input); i++) {
        printf("%02x ", input[i]);
    }
    printf("\n");
    printf("first_bytes: ");
    for (int i = 0; i < strlen(first_bytes); i++) {
        printf("%02x ", first_bytes[i]);
    }
    printf("\n");
    printf("second_bytes: ");
    for (int i = 0; i < strlen(second_bytes); i++) {
        printf("%02x ", second_bytes[i]);
    }
    printf("\n");
    printf("third_bytes: ");
    for (int i = 0; i < strlen(third_bytes); i++) {
        printf("%02x ", third_bytes[i]);
    }
    printf("\n");

    // Apply inverse operations in reverse order
    xor_byte(input, third_bytes);
    decrease_I(input, 0xf3);
    increase_I(input, 0x4d);
    xor_byte(input, second_bytes);
    increase_I(input, 0x5a);
    decrease_I(input, 0x1f);
    xor_byte(input, first_bytes);

    // Print the resulting input array
    for (int i = 0; i < 0x20; i++) {
        printf("%02x ", input[i]);
    }
    printf("\n");

    return 0;
}

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 加密函数
void caesar_encrypt(char *plaintext, int shift) {
    int i;
    int len = strlen(plaintext);
    for (i = 0; i < len; i++) {
        if (plaintext[i] >= 'a' && plaintext[i] <= 'z') {
            plaintext[i] = ((plaintext[i] - 'a') + shift) % 26+ 'a';
        } else if (plaintext[i] >= 'A' && plaintext[i] <= 'Z') {
            plaintext[i] = ((plaintext[i] - 'A') + shift) % 26 + 'A';
        }
    }
}

// 解密函数
void caesar_decrypt(char *ciphertext, int shift) {
    int i;
    int len = strlen(ciphertext);
    for (i = 0; i < len; i++) {
        if (ciphertext[i] >= 'a' && ciphertext[i] <= 'z') {
            ciphertext[i]=(ciphertext[i] - 'a' - shift + 26) % 26 + 'a';
        } else if (ciphertext[i] >= 'A' && ciphertext[i] <= 'Z') {
            ciphertext[i]=(ciphertext[i] - 'A' - shift + 26) % 26+ 'A';
        }
    }
}

int main() {
    char plaintext[] = "Hello, World!";
    int shift = 3;

    char encrypted[100];
    strcpy(encrypted, plaintext);
    caesar_encrypt(encrypted, shift);
    printf("加密后的文本: %s\n", encrypted);

    char decrypted[100];
    strcpy(decrypted, encrypted);
    caesar_decrypt(decrypted, shift);
    printf("解密后的文本: %s\n", decrypted);

    return 0;
}
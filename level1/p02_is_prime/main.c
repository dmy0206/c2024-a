#include <stdio.h>
#include "stdbool.h"
int main() {
    int c;
    bool flag;
    flag = false;
    scanf_s("%d", &c);
    for (int x = 2; x < c; x++)
        if (c % x == 0) {
            flag = true;
        }
    printf("%s\n", flag ? "true" : "false");
    return 0;
}
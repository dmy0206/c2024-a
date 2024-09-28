#include <stdio.h>
#include<time.h>
#include "stdbool.h"
bool is_prime(int c) {
    bool flag;
    flag = true;
    for (int x = 2; x < c; x++)
        if (c % x == 0) {
            flag = false;
        }
    return flag;
}
int main() {
    time_t start, end;
    int arr[100] = {};
    start = time(NULL);
    for (int i = 2; i < 100; i++)
        if (is_prime(i)) {
            printf("%d  ", i);
        };
    end = time(NULL);
    int time;
    time = end - start;
    printf("%d", &time);
    return 0;
}
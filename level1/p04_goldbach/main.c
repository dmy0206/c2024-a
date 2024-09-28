#include <stdio.h>
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
    int arr[100] = {};
    int count=0;
    for (int i = 2; i < 100; i++)
        if (is_prime(i)) {
            arr[count]=i;
            count++;
        }
//    for(int i=0;i<=10;i++){
//        printf("%d",arr[i]);
//    };
int arr1[100]={};
for(int i;i<=count;i++){
    arr[]
}
    return 0;
}
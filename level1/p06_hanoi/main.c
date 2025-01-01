#include <stdio.h>
void move(int n, char from, char to) {
    printf("将第 %d 个盘子从 %c 移动到 %c\n", n, from, to);
}

void hanoi(int n, char source, char auxiliary, char destination) {
    if (n == 1) {
        move(1, source, destination);
    } else {
        hanoi(n - 1, source, destination, auxiliary);
        move(n, source, destination);
        hanoi(n - 1, auxiliary, source, destination);
    }
}

int main() {
    int num_disks;
    printf("请输入汉诺塔盘子的数量: ");
    scanf("%d", &num_disks);
    hanoi(num_disks, 'A', 'B', 'C');
    return 0;
}
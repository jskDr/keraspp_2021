#include <stdio.h>

// a function to calculate the sum from 0 to N-1
int my_sum(int N) {
    // N is the maximum number of digits in the sum
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += i;
    }
    return sum;
}

int main() {
    // call a function to calculate sum from 0 to 9
    int sum = my_sum(10);
    printf("Sum(10) = %d\n", sum);
    return 0;
}

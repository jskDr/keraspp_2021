#include <stdio.h>

int fibo(int n) {
    if (n < 2) {
        return n;
    } else {
        return fibo(n-1) + fibo(n-2);
    }
}

int main() {
    printf("%d\n", fibo(45));
    return 0;
}

#include <iostream>

int fibo(int n) {
    if (n < 2) {
        return n;
    } else {
        return fibo(n-1) + fibo(n-2);
    }
}

int main() {
    std::cout << fibo(45) << std::endl;
    return 0;
}

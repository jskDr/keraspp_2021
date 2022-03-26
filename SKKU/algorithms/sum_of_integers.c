#include <stdio.h>
unsigned long int sum_of_integers(unsigned int n) {
    unsigned int i;
    unsigned long int sum = 0;
    for(i=0;i<n;i++)
    {
        sum = sum + i;
    }
    return sum;
}

void main() {
    // unsigned int n = 10000;
    unsigned int n = 1000000;
    unsigned long int sum_theory = (unsigned long int) n*(n-1)/2;
    unsigned long int sum = sum_of_integers(n);
    printf("Sum = %lu = %lu\n", sum_theory, sum);
}

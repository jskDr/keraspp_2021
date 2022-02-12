#include <stdio.h>

double vectorMean(int *arr, int n)
{
    int i, sum=0;
    double mean;
    for (i=0; i<n; i=i+1)
        sum = sum + arr[i];
    mean = sum / (double)n;
    return mean;
}

// gcc -Wall -shared -o myC.so mean.c
/*
void main() {
    int p_a[] = {1,2,3};
    double m;
    m = vectorMean(p_a, 3);
    printf("%f\n", m);
}
*/
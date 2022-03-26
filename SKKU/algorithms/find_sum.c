#include <stdio.h>

float FindSum(float list[], int n)
{  
    float sum = 0;
    int i;
    for (i = 0; i < n; i++)
        sum += list[i];
    return sum;
}

void main() {
    float list[] = {10.5, 4.8, 13.2, 6.4, 9.5};
    int n = 5;
    float sum = FindSum(list, n);

    printf("Sum = %f\n", sum);
}
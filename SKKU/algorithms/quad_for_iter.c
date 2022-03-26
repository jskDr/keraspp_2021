#include <stdio.h>

void main() {
    int sum = 0;
    int n = 10;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++) 
            for (int k = 0; k < j; k++) 
                sum++;
    printf("Total complexiity: %d\n", sum);
}

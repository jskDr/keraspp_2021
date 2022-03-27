#include <stdio.h>

int removeDuplicates(int* nums, int numsSize){
    int i, j = 0;
    for (i=1; i<numsSize; i++) {
        if (nums[j] < nums[i]) {
            j++;
            if (i > j) {
                nums[j] = nums[i];
            }
        }
    }
    return j+1;
}

#define numsSize  9
void main() {
    int nums[numsSize] = {1, 1, 2, 2, 3, 4, 4, 4, 5};
    int newNumsSize;
    int i;
    newNumsSize = removeDuplicates(nums, numsSize);
    for(i=0;i<newNumsSize;i++) {
        printf("%d\n", nums[i]);
    }
}
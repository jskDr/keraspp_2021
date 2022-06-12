#include <stdio.h>
#include <string.h>

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
void main_1() {
    int nums[numsSize] = {1, 1, 2, 2, 3, 4, 4, 4, 5};
    int newNumsSize;
    int i;
    newNumsSize = removeDuplicates(nums, numsSize);
    for(i=0;i<newNumsSize;i++) {
        printf("%d\n", nums[i]);
    }
}

int strStr(char * haystack, char * needle){
    int i, j, lh, ln, fnd = -1;
    lh = strlen(haystack);
    ln = strlen(needle);
    if(ln > 0) {
        for(i=0; i<lh-ln+1; i++) {
            // compare
            for(j=0; j<ln; j++) {
                // printf("%c <-> %c, %d, %d\n", haystack[i+j],  needle[j], j, ln);
                if(haystack[i+j] != needle[j]) {
                    // printf("break!\n");
                    break;
                }
            }
            if(j == ln) {
                fnd = i;
                break;
            }      
        }
    }
    else {
        fnd = 0;
    }
    return fnd;
}

void main() {
    char *s1 = "mississippi";
    char *s2 = "issip";
    int a;
    a = strStr(s1, s2);
    printf("%d", a);
}
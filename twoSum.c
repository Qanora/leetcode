#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* twoSum(int* nums, int numsSize, int target);


int main()
{
    int b[3] = {3,2,4};
    int *a = twoSum(b,3,6);
    printf("%d %d",a[0],a[1]);
    return 0;
}

int* twoSum(int* nums, int numsSize, int target)
{
    int i = 0, j = 0;
    int* a;
    a = (int*)malloc(sizeof(int)*2);
    for(i = 0; i < numsSize; i++)
    {
        printf("%d",*(nums+i));
        for(j = i+1; j < numsSize; j++)
        {
            printf("%d\n",*(nums+j));
            if(*(nums+i)+*(nums+j) == target)
            {
                *a = i;
                *(a+1) = j;
                return a;
            }
        }
    }
    return a;
}


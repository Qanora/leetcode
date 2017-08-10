#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int removeElement(int* nums, int numsSize, int val);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    int a[] = {2,2,2};
    int count = removeElement(a,3,2);
    printf("count = %d\n",count);
    int i = 0;
    for(i = 0; i < count; i++)
    {
        printf("%d ",a[i]);
    }
    printf("\n");
    return 0;
}
int removeElement(int* nums, int numsSize, int val)
{
    int i = 0;
    int j = 0;
    int k = 0;
    for(i = 0; i < numsSize - 1; i++)
    {
        if(*(nums+i) == val)
        {
            for(j = i; j < numsSize - 1; j++)
            {
                *(nums+j) = *(nums+j+1);
            }
            numsSize--;
            i--;
        }
    }
    if(*(nums+i) == val)
    {
        numsSize--;
    }
    if(numsSize == 0) nums = NULL;
    return numsSize;
}

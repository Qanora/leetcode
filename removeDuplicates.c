#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int removeDuplicates(int* nums, int numsSize);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    int a[] = {1,1};
    int count = removeDuplicates(a,2);
    printf("count = %d\n",count);
    int i = 0;
    for(i = 0; i < count; i++)
    {
        printf("%d",a[i]);
    }
    printf("\n");
    return 0;
}
int removeDuplicates(int* nums, int numsSize)
{
    if(numsSize == 0) return 0;
    if(numsSize <= 1) return 1;
    int count = removeDuplicates(nums+1, numsSize-1);
    if(*nums != *(nums+1)) 
    {
        printf("nums=%d nums+1=%d\n",*nums,*(nums+1));
        count++;
        return count;
    }
    else
    {
        int i = 0;
        for(i = 0; i < numsSize -1; i++)
        {
            *(nums+i) = *(nums+i+1);
        }
    }
    return count;
}

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int** threeSum(int* nums, int numsSize, int* returnSize);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    int returnSize = 0;
    int temp[] = {-1,0,1,2,-1,-4};
    int i = 0;
    for(i = 0; i < 6; i++)
    {
        printf("%d ",temp[i]);
    }
    int** result;
    result = threeSum(temp,6,&returnSize);
    printf("size = %d\n",returnSize);
    for(i = 0; i < returnSize; i++)
    {
        printf("[%d %d %d]\n",result[i][0],result[i][1],result[i][2]);
    }
    return 0;
}
int** threeSum(int* nums, int numsSize, int* returnSize)
{
    qsort(nums,numsSize,sizeof(int),cmpfunc);
    int lo = 0, hi = numsSize-1, sum = 0;
    int i = 0;
    int count = 0;
    for(i = 0; i < numsSize - 2; i++)
    {

        lo = i+1;
        hi = numsSize - 1;
        sum = 0 - nums[i];
        if(i == 0 || (i > 0 && nums[i] != nums[i-1]))
        {
            while(lo < hi)
            {
                if(sum == nums[lo] + nums[hi])
                {
                    while(lo < hi && nums[lo] == nums[lo+1]) lo++;
                    while(lo < hi && nums[hi] == nums[hi-1]) hi--;
                    count++;
                    lo++;
                    hi--;
                }
                else if(sum < nums[lo] + nums[hi])
                {
                    hi--;
                }
                else
                {
                    lo++;
                }
            }
        }

    }
    int** temp = (int**) malloc(sizeof(int*)*count);
    for(i = 0; i < count; i++)
    {
        temp[i] = malloc(sizeof(int)*3);
    }
    *returnSize = count;
    count = 0;
    for(i = 0; i < numsSize - 2; i++)
    {

        lo = i+1;
        hi = numsSize - 1;
        sum = 0 - nums[i];
        if(i == 0 || (i > 0 && nums[i] != nums[i-1]))
        {
            while(lo < hi)
            {
                if(sum == nums[lo] + nums[hi])
                {
                    temp[count][0] = nums[i];
                    temp[count][1] = nums[lo];
                    temp[count++][2] = nums[hi];
                    while(lo < hi && nums[lo] == nums[lo+1]) lo++;
                    while(lo < hi && nums[hi] == nums[hi-1]) hi--;
                    lo++;
                    hi--;
                }
                else if(sum < nums[lo] + nums[hi])
                {
                    hi--;
                }
                else
                {
                    lo++;
                }
            }
        }

    }
    return temp;
}

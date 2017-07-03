#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int** fourSum(int* nums, int numsSize,int target, int* returnSize);
int** threeSum(const int* nums, int numsSize, int target, int* returnSize);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    int returnSize = 0;
    int temp[] = {0,1,5,0,1,5,5,-4};
    int i = 0;
    for(i = 0; i < 8; i++)
    {
        printf("%d ",temp[i]);
    }
    int** result;
    result = fourSum(temp,8,11,&returnSize);
    printf("size = %d\n",returnSize);
    for(i = 0; i < returnSize; i++)
    {
        printf("[%d %d %d %d]\n",result[i][0],result[i][1],result[i][2],result[i][3]);
    }
    return 0;
}
int** fourSum(int* nums, int numsSize,int target, int* returnSize)
{
   qsort(nums,numsSize,sizeof(int),cmpfunc);
   int i = 0;
   int sum = 0;
   int count = 0;
   int size = 0;
   for(i = 0; i < numsSize - 3; i++)
   {
        while(i - 1 >= 0 && nums[i] == nums[i-1]) i++;
        sum = target - nums[i];
        threeSum(nums+i+1, numsSize-i-1, sum, &size);
        count += size;
   }
   int** result = (int**)malloc(sizeof(int*)*count);
   for(i = 0; i < count; i++)
   {
        result[i] = malloc(sizeof(int)*4);
   }
   size = 0;
   count = 0;
   int j = 0;
   int k = 0;
   int l = 0;
   int** temp;
   for(i = 0; i < numsSize - 3; i++)
   {
        while(i - 1 >= 0 && nums[i] == nums[i-1]) i++;
        sum = target - nums[i];
        temp = threeSum(nums+i+1, numsSize-i-1, sum, &size);
        for(j = 0; j < size; j++)
        {
            result[count][0] = nums[i];
            for(k = 0; k < 3; k++)
            {
                result[count][k+1] = temp[j][k];
            }
            count++;
        }
        for(l = 0; l < size; l++)
        {
            free(temp[l]);
        }
        if(temp != NULL) free(temp);
   }
    *returnSize = count;
   return result;

   
}
int** threeSum(const int* nums, int numsSize,int target, int* returnSize)
{
    int lo = 0, hi = numsSize-1, sum = target;
    int i = 0;
    int count = 0;
    for(i = 0; i < numsSize - 2; i++)
    {

        lo = i+1;
        hi = numsSize - 1;
        sum = target - nums[i];
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
    if(count == 0) return NULL;
    count = 0;
    for(i = 0; i < numsSize - 2; i++)
    {

        lo = i+1;
        hi = numsSize - 1;
        sum = target - nums[i];
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

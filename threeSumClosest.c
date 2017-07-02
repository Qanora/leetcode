#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int threeSumClosest(int* nums, int numsSize, int target);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    int temp[] = {1,1,1,0};
    printf("%d\n",threeSumClosest(temp,4,100));
    return 0;
}
int threeSumClosest(int* nums, int numsSize, int target)
{
    qsort(nums,numsSize,sizeof(int),cmpfunc);
    int lo = 0, hi = numsSize-1, sum = target;
    int i = 0;
    int min = INT_MAX;
    int temp = 0;
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
                    return target;
                }
                else if(sum < nums[lo] + nums[hi])
                {
                    if(min > abs(nums[i]+nums[lo]+nums[hi]-target))
                    {
                        temp = nums[i]+nums[lo]+nums[hi];
                        min = abs(nums[i]+nums[lo]+nums[hi]-target);         
                    }
                    hi--;
                }
                else
                {
                    if(min > abs(nums[i]+nums[lo]+nums[hi]-target))
                    {
                        temp = nums[i]+nums[lo]+nums[hi];
                        min = abs(nums[i]+nums[lo]+nums[hi]-target);
                    }
                    lo++;
                }
            }
        }
    }
    return temp;
}

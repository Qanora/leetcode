#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<stdint.h>
#include<limits.h>
#define min(x,y) (x > y ? y:x)
#define max(x,y) (x > y ? x:y)
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size);
double findMedianSortedArrays_adv(int* nums1, int nums1Size, int* nums2, int nums2Size);
double findSingleArrarys(int* nums1,int nums1Size);
int main()
{
    int a[2] = {1,3};
    int b[2] = {1,2};
    printf("%f\n",findMedianSortedArrays_adv(a,2,b,2));
    return 0;
}
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
    int i = 0, j = 0;
    int count = 0;
    int rest = (nums1Size + nums2Size)%2;
    int avg = (nums1Size + nums2Size)/2;
    double davg = (double)(nums1Size + nums2Size)/2;
    int flagI = nums1Size == 0;
    int flagJ = nums2Size == 0;
    int temp = 0;
    int lastTemp = 0;
    double Median = 0;
    while(1)
    {
        if(count >= davg )  break;
        printf("count = %d davg= %f\n",count,davg);
        printf("nums1=%d nums2=%d\n",*(nums1+i),*(nums2+j));
        if(!flagJ && (*(nums1+i) >= *(nums2+j) || flagI))
        {
            if(j < nums2Size -1)
            {
                temp = nums2[j];
                j++;
            }
            else
            {
                flagJ=1;
                temp = nums2[j];
            }
            count++;
        }
        printf("temp = %d\n",temp);
        if(count >= davg ) break;
        if(!flagI && (*(nums1+i) <= *(nums2+j) || flagJ))
        {
            if(i < nums1Size -1)
            {
                temp = nums1[i];
                i++;
            }
            else
            {
                flagI=1;
                temp = nums1[i];
            }
            count++;
        }
    }
    printf("flagI = %d, flagJ = %d\n",flagI, flagJ);
    printf("i=%d j=%d\n",i,j);
    if(flagI && !flagJ)
    {
        lastTemp = nums2[j];
    }
    else if(flagJ && !flagI)
    {
        lastTemp = nums1[i];
    }
    else if(!flagJ && !flagI)
    {
        printf("i = %d, j = %d\n",i,j);
        lastTemp = nums1[i] > nums2[j] ? nums2[j] : nums1[i];
    }
    else if(flagJ && flagI)
    {
        lastTemp = nums1[i] > nums2[j] ? nums2[j] : nums1[i];
    }
    printf("temp = %d\n",temp);
    printf("i=%d, j=%d\n",i,j);
    printf("lastTemp = %d\n",lastTemp);
    Median = rest ? temp : (double)(temp+lastTemp)/2;
    return Median;
}
double findMedianSortedArrays_adv(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
    if(nums1Size == 0)
    {
        findSingleArrarys(nums2,nums2Size);
    }
    else
    {
        findSingleArrarys(nums1,nums1Size);
    }
    if(nums1Size > nums2Size)
    {
        return findMedianSortedArrays_adv(nums2,nums2Size,nums1,nums1Size);
    }
    int L1,L2,R1,R2,c1,c2,lo = 0, hi = 2 * nums1Size;
    while(lo <= hi)
    {
        c1 = (lo+hi)/2;
        c2 = nums1Size + nums2Size-c1;
        L1 = (c1 == 0) ? INT_MIN: nums1[(c1-1)/2];
        R1 = (c1 == 2*nums1Size) ? INT_MAX: nums1[c1/2];
        L2 = (c2 == 0) ? INT_MIN: nums2[(c2-1)/2];
        R2 = (c2 == 2*nums2Size) ? INT_MAX: nums2[c2/2];
        if(L1 > R2)
        {
            hi = c1 - 1;
        }
        else if(L2 > R1)
        {
            lo = c1 + 1;
        }
        else break;
    }
    printf("L1=%d, L2=%d, R1=%d, R2=%d\n",L1,L2,R1,R2);
    printf("max=%d min=%d\n",max(L1,L2),min(R1,R2));
    return (max(L1,L2)+min(R1,R2))/2.0;

}
double findSingleArrarys(int* nums1,int nums1Size)
{
    if(nums1 == 0) return -1;
    return (nums1[(nums1Size-1)/2] + nums1[nums1Size/2])/2.0;
}

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int maxArea(int* height,int heightSize);

int main()
{
    int a[] = {1,2,1};
    maxArea(a,3);
    return 0;
}
/*int maxArea(int* height,int heightSize)
{
    int i = 0;
    int j = 0;
    int max = 0;
    int temp = 0;
    for(i = 0; i < heightSize; i++)
    {
        for(j = i+1; j < heightSize; j++)
        {
            temp = min(*(height+i),*(height+j))*(j-i);
            printf("temp = %d",temp);
            if(max < temp)
            {
                max = temp;
            }
        }
    }
    return max;
}*/
int maxArea(int* height, int heightSize)
{
    int i = 0;
    int j = heightSize - 1;
    int maxArea = 0;
    while(i < j)
    {
        maxArea = max(maxArea,min(*(height+i),*(height+j))*(j-i));
        if(*(height+i) < *(height+j))
        {
            i++;
        }
        else
        {
            j--;
        }
    }
    return maxArea;
}

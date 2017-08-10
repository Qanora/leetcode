#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    return 0;
}
int divide(int dividend, int divisor)
{
    long temp1 = dividend;
    long temp2 = divisor;
    long result = dividend;
    if(divisor == 0) return INT_MAX;
    else if(temp1 >= INT_MIN && temp1 <= INT_MAX && temp2 >= INT_MIN && temp2 <= INT_MAX)
    {
        result = (double)dividend/divisor;
        if(result <= INT_MAX && result >= INT_MIN)
        {
            return result;
        }
        else
        {
            return INT_MAX;
        }
    }
    return INT_MAX;
}

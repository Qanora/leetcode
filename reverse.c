#include<limits.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int reverse(int x);

int main()
{
    reverse(123456);
    return 0;
}
int reverse(int x)
{
    long long res = 0;
    while(x)
    {
        res = res * 10 + x % 10;
        x = x / 10;
    }
    res = res < INT_MIN ? INT_MIN : res;
    res = res > INT_MAX ? INT_MAX : res;
    return res;
}

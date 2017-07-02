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


#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
void change(char* s);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    char* s = malloc(sizeof(char)*2);
    *s = '4';
    *(s+1) = '\0';
    printf("%s\n",s);
    change(s);
    printf("%s",s);
    return 0;
}
void change(char* s)
{
    char* v = malloc(sizeof(char)*2);
    *v = '5';
    *(v+1) = '\0';
    s = v;
}

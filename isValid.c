#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
bool isValid(char* s);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    char s[] = ")){{";
    if(isValid(s)) printf("TRUE");
    return 0;
}
bool isValid(char* s)
{
    int len = strlen(s);
    int i = 0;
    int count = 0;
    for(i = 0; i < len; i++)
    {
        if(s[i] == '(' || s[i] == ')' || s[i] == '[' || s[i] == ']' || s[i] == '{' || s[i] == '}' )
        {
            count++;
        }

    }
    char* temp = malloc(sizeof(char)*count);
    int* cent = malloc(sizeof(int)*count);
    count = 0;
    for(i = 0; i < len; i++)
    {
        if(s[i] == '(' || s[i] == ')' || s[i] == '[' || s[i] == ']' || s[i] == '{' || s[i] == '}' )
        {
            temp[count++] = s[i];
        }       
    }
    int centV = 2;
    int countV = 0;
    int countL = 0;
    int countR = 0;
    for(i = 0; i < count; i++)
    {
        if(temp[i] == '(' || temp[i] == '[' || temp[i] == '{')
        {
            cent[countV++] = centV++;
            countL++;
        }
        if(temp[i] == ')' || temp[i] == ']' || temp[i] == '}')
        {
            cent[countV++] = --centV;
            countR++;
        }
    }
    long result = 0;
    for(i = 0; i < count ; i++)
    {
        if(temp[i] == '(') result += 1*cent[i];
        if(temp[i] == '[') result += 10*cent[i];
        if(temp[i] == '{') result += 100*cent[i];
        if(temp[i] == ')') result -= 1*cent[i];
        if(temp[i] == ']') result -= 10*cent[i];
        if(temp[i] == '}') result -= 100*cent[i];
    }
    free(temp);
    free(cent);
    printf("%ld\n",result);
    return !result && countL == countR;
}

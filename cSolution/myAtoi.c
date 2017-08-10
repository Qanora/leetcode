#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
long unsignedAtoi(char* str,int flag,int flag2);
int myAtoi(char* str);
int main()
{
    printf("%d\n",myAtoi("-184467440737095516170"));
    return 0;
}
int myAtoi(char* str)
{
    int len = strlen(str);
    if(!len)  return 0;
    long res = 0;
    int i = 0;
    int flag = 1;
    char* tempAdd = memchr(str,'+',strlen(str));
    char* tempSub = memchr(str,'-',strlen(str));
    if(tempAdd != NULL && tempSub != NULL)
    {
        return 0;
    }
    if(tempAdd == NULL && tempSub == NULL)
    {
        res = unsignedAtoi(str,0,0);
        if(res > INT_MAX) res = INT_MAX;
        if(res < INT_MIN) res = INT_MAX;
    }
    if(tempSub != NULL)
    {
        res = unsignedAtoi(tempSub+1,1,1);
        flag = -1;
        res = res*flag;
        if(res > INT_MAX) res = INT_MIN;
        if(res < INT_MIN) res = INT_MIN;

    }
    if(tempAdd != NULL)
    {
        res = unsignedAtoi(tempAdd+1,1,0);
        if(res > INT_MAX) res = INT_MAX;
        if(res < INT_MIN) res = INT_MAX;

    }
    printf("text = %ld\n",res);
    return res;
}

long unsignedAtoi(char* str, int flag,int flag2)
{
    int len = strlen(str);
    int i = 0;
    long res = 0;
    for(; i < len; i++)
    {
        if((*(str+i) > '9' || *(str+i) < '0') && *(str+i) != ' ') return res;
        if(*(str+i) == ' ' && (res || flag))
        {
            return res;
        }

        if(*(str+i) >= '0' && *(str+i) <= '9')
        { 
            res = res*10 + *(str+i)-'0';
            if(res > INT_MAX && !flag2) return INT_MAX;
            if(res - 1> INT_MAX && flag2)
            { 
                printf("adf");
                return INT_MIN;
            }
            flag = 1;
        }
    }
    return res;
}

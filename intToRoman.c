#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#include<ctype.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
char* intToRoman(int num);
int main()
{
    printf("%s",intToRoman(3999));
    return 0;
}

char* intToRoman(int num)
{
    char a[100];
    char s[] = "I1V2X3L4C5D6M";
    int p[] = {1,4,5,9,10,40,50,90,100,400,500,900,1000};
    int pLen = strlen(s);
    int i = 0;
    int count = 0;
    while(num)
    {
        for(i = pLen -1; i >= 0 ; i--)
        {
            while(num/p[i])
            {
                num = num - p[i];
                a[count++] = s[i];
            }
        }
    }
    a[count] = '\0';
    int nLen = 0;
    for(i = 0; i < count; i++)
    {
        if(a[i] >= '0' && a[i] <= '9') nLen++;
    }
    int temp = 0;
    char* send = malloc(sizeof(char)*(count+nLen+1));
    for(i = 0; i < count; i++)
    {
        if(a[i] >= '0' && a[i] <= '9')
        {
            if(a[i] == '1')
            {
                *(send+temp++) = 'I';
                *(send+temp++) = 'V';
            }
            if(a[i] == '2')
            {
                *(send+temp++) = 'I';
                *(send+temp++) = 'X';
            }
            if(a[i] == '3')
            {
                *(send+temp++) = 'X';
                *(send+temp++) = 'L';
            }
            if(a[i] == '4')
            {
                *(send+temp++) = 'X';
                *(send+temp++) = 'C';
            }
            if(a[i] == '5')
            {
                *(send+temp++) = 'C';
                *(send+temp++) = 'D';
            }
            if(a[i] == '6')
            {
                *(send+temp++) = 'C';
                *(send+temp++) = 'M';
            }

        }
        else
        {
            *(send+temp++) = a[i];
        }
    }
    *(send+temp) = '\0';
    return send;
}


#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    int sLen = 10;
    int pLen = 11;
    int **p;
    p = (int**) malloc (sizeof(int*)*sLen);
    int i = 0;
    for(i = 0; i < sLen; i++)
    {
        *(p+i) = (int*) malloc(sizeof(int)*pLen);
        memset(*(p+i),0,sizeof(int)*pLen);
    }
    int j = 0;
    for(i = 0; i < sLen; i++)
    {
        
        for(j = 0; j < pLen; j++)
        {
            printf("%d",p[i][j]);
        }
    }
}

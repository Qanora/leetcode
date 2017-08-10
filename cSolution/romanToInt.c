#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int romanToInt(char* s);
int main()
{
    printf("%d\n",romanToInt("MMMCMXCIX"));
    return 0;
}

int romanToInt(char* s)
{
    int n = 0;
    int last = 2000;
    char compC[] = "IVXLCDM";
    int compN[] = {1,5,10,50,100,500,1000};
    int sLen = strlen(s);
    int pLen = strlen(compC);
    int i = 0;
    int j = 0;
    for(i = 0; i < sLen; i++)
    {
        for(j = 0; j < pLen; j++)
        {
            if(*(s+i) == *(compC+j))
            {
                if(last < *(compN+j))
                {
                    n -= last*2;
                }
                last = *(compN+j);
                n += compN[j];
                n = abs(n);

            }
        }
    }
    return n;
}

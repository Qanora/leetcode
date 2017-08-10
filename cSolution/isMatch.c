#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
#define printTF(x) (x ? printf("TRUE  "): printf("FALSE "))
bool isMatch(char* s, char* p);
char* getCheck(char* temp);
int main()
{
    char s[] = "aab";
    char p[] = "c*a*b";
    printTF(isMatch(s,p));
    return 0;
}
/*bool isMatch(char* s, char* p)
{
    int sLen = strlen(s)+1;
    int pLen = strlen(p)+1;
    int** dp = (int**) malloc(sizeof(int*)*sLen);
    int i = 0;
    for(i = 0; i < sLen; i++)
    {
        *(dp+i) = (int*) malloc(sizeof(int)*pLen);
        memset(*(dp+i),0,sizeof(int)*pLen);
    }
    int j = 0;
    dp[0][0] = 1;
    for(i = 0; i < pLen-1; i++)
    {
        if(*(p+i) == '*' && dp[0][i-1])
        {
            dp[0][i+1] = 1;
        }
    }
    for(i = 0; i < sLen-1; i++)
    {
        for(j = 0; j < pLen-1; j++)
        {
            if(*(p+j) == '.')
            {
                dp[i+1][j+1] = dp[i][j];
            }
            if(*(s+i) == *(p+j))
            {
                dp[i+1][j+1] = dp[i][j];
            }
            if(*(p+j) == '*')
            {
                if(*(p+j-1) != *(s+i) && *(p+j-1) != '.')
                {
                    dp[i+1][j+1] = dp[i+1][j-1];
                }
                else
                {
                    printf("******%d %d %d\n",dp[i+1][j],dp[i][j+1],dp[i+1][j-1]);
                    dp[i+1][j+1] = dp[i+1][j] || dp[i][j+1] || dp[i+1][j-1];    
                }
            }

        }
    }
    for(i = 0; i < sLen-1; i++)
    {
        for(j = 0; j < pLen-1; j++)
        {
            printf("%d ",dp[i][j]);
        }
        printf("\n");
    }
    int res = dp[sLen-1][pLen-1];
    for(i = 0; i < sLen; i++)
    {
        free(*(dp+i));
    }
    free(dp);
    if(res == 0) return false;
    return true;
}*/

bool isMatch(char* s, char* p)
{
    if(!*p) return !*s; // match one or many
    if(*(p+1) == '*')
    {
        if(*s && (*p == *s || *p == '.'))
        {
            return (isMatch(s+1,p+2) || isMatch(s+1,p) || isMatch(s,p+2));
        }
        else
        {
            return isMatch(s,p+2);
        }
    }
    if(*s && (*p == *s || *p == '.'))
    {
        return isMatch(s+1,p+1);
    }
    return false;
}

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int lengthOfLengestSubstring(char* a);
int main()
{
    char *a = "adsfa";
    printf("%d",lengthOfLengestSubstring(a));
}

int lengthOfLengestSubstring(char* a)
{
    int flag[200];
    memset(flag,-1,sizeof(flag));
    int m = -1;
    int max = 0;
    int count = 0;
    while(*a){
        m = flag[*a] > m ? flag[*a] : m;
        flag[*a] = count;
        max = max > count - m ? max : count - m;
        printf("char=%c m=%d count=%d max=%d\n",*a,m,count,max);
        count++;
        a++;
    }
    if(m == -1) max=count;
    return max;
}

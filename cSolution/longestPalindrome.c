#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char* longestPalindrome(char* s);
char* findLongest(const char* s, int i, int j);
int main()
{
    char* s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb";
    printf("%s\n",longestPalindrome(s));
}

char* longestPalindrome(char* s)
{
    int i = 0;
    int max = 0;
    int start = 0;
    int end = 0;
    int k = 0;
    int flag = 0;
    int len = strlen(s);
    for(i = 0; i < len; i++)
    {
        while(i - k >= 0 && *(s+i-k) == *(s+i+k))
        {
            k++;
        }
        if(max < k - 1)
        {
            max = k - 1;
            start = i - max;
        }
        k = 0;
    }
    for(i = 0; i < len; i++)
    {
        while(i - k >= 0 && *(s+i-k) == *(s+1+i+k))
        {
            k++;
        }
        if(max <= k - 1)
        {
            flag = 1;
            max = k - 1;
            start = i - max;
        }
        k = 0;
    }
    end = start+max*2;
    char* temp = malloc(sizeof(char)*(end+flag-start+2));
    k = 0;
    printf("%d %d",start,end+flag);
    for(i = start; i <= end+flag; i++)
    {
        temp[k++] = *(s+i);
    }
    printf("\nk = %d\n",k);
    temp[k]='\0';
    return temp;
}

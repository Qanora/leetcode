#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
int strStr(char* haystack, char* needle);
int strStrs(char* haystack, char* needle);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    //          0123456789
    char s[] = "mississippi";
    char n[] = "sipp";
    int count = strStrs(s,n);
    printf("count =%d\n",count);
    return 0;
}
int strStrs(char* haystack, char* needle) 
{
    
 if (!haystack || !needle) return -1;
        for (int i = 0; ; ++i) {
            for (int j = 0; ; ++j) {
                if (needle[j] == 0) return i;
                if (haystack[i + j] == 0) return -1;
                if (haystack[i + j] != needle[j]) break;
            }
        }
}
int strStr(char* haystack, char* needle)
{
    if(haystack == NULL || needle == NULL) return 0;
    int lenH = strlen(haystack);
    int lenN = strlen(needle);
    if(lenH == 0 && lenN == 0) return 0;
    int i = 0;
    int j = 0;
    bool flag = true;
    bool sec = true;
    int count = 0;
    for(i = 0; i < lenH; i++)
    {
        flag = true;
        sec = true;
        for(j = 0; j < lenN; j++)
        {
            if(flag && *(haystack+i+j) != *(needle+j))
            {
                flag = false;
                break;
            }
            else
            {
                if(sec && j != 0 && *(haystack+i+j) == *(needle))
                {
                    sec = false;
                    count = i + j - 1;
                }
            }
        }
        if(flag) return i;
        if(count >= i)
        {
            i = count;
        }
        else
        {
            if(i+j-2 > i)
            {
                i = i + j - 2;
            }
        }
    }
    return -1;
}

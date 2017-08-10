#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
char* longestCommonPrefix(char strs[][1], int strsSize);
int main()
{
    char s[2][1] = {"a","b"};
    printf("%s\n",longestCommonPrefix(s,2));
    return 0;
}

char* longestCommonPrefix(char strs[][1], int strsSize)
{
    if(strsSize == 0) return "";
    char prefix[100];
    int count = 0;
    int len = INT_MAX;
    int i = 0;
    int j = 0;
    char temp;
    for(i = 0; i < strsSize; i++)
    {
        len = min(len,strlen(strs[i]));
    }
    for(i = 0; i < len; i++)
    {
        temp = strs[0][i];
        for(j = 0; j < strsSize; j++)
        {
            if(temp != strs[j][i])
            {
                if(i == 0) return "";
                char* send = malloc(sizeof(char)*(count));
                strcpy(send,prefix);
                *(send+count) = '\0';
                return send;
            }
        }
        prefix[count++] = strs[0][i];
    }
}


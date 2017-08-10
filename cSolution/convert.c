#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
char* convert(char* s, int numsRows);
int main()
{
    char *s = "A";
    printf("%s\n",convert(s,1));
    return 0;
}
char* convert(char* s, int numsRows)
{
    int frow = 0;
    int i = 0;
    int j = 0;
    int len = strlen(s);
    int stack = (numsRows-1)*2;
    char* temp = malloc(sizeof(char)*len+1);
    int count=0;
    for(i = 0; i < numsRows; i++)
    {
        j = i;
        while(j < len)
        {   
            if((stack - i*2 && j < len) != 0) temp[count++] = *(s+j);
            j += stack - i*2;
            if(i != 0 && j < len ) temp[count++] = *(s+j);
            j += i*2;
        }

    }
    temp[count] = '\0';
    return temp;
}

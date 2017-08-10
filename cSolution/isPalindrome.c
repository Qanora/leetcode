#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
bool isPalindrome(int x);
int main()
{
    if(isPalindrome(111)) printf("TRUE");
    else printf("FLASE");
    return 0;
}
bool isPalindrome(int x)
{
    if(x < 0) return false;
    char buffer[30];
    sprintf(buffer,"%d",x);
    printf("%s\n",buffer);
    int len = strlen(buffer);
    len = len -1;
    printf("%d\n",len);
    int i = 0;
    while(len-i >= i)
    {
        printf("len-i =%d\n",len-i);
        printf("buffer_h=%c, buffer_f=%c\n",buffer[i],buffer[len-i]);
        if(buffer[i] == buffer[len-i]) i++;
        else return false;
        
    }
    return true;
} 

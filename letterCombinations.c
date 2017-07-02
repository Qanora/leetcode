#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
char** make(char** input1, int* size, char* input2, int row);
char** letterCombinations(char* digits, int* returnSize);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    char letter[] = "34";
    int size = 0;
    char** temp = letterCombinations(letter,&size);
    int i = 0;
    for(i = 0; i < size; i++)
    {
        printf("%s\n",temp[i]);
    }
    return 0;
}
char** letterCombinations(char* digits, int* returnSize)
{
    if(strlen(digits) == 0) return NULL;
    int i = 0;
    char** letter = malloc(sizeof(char*)*8);
    for(i = 0; i < 5; i++)
    {
        letter[i] = malloc(sizeof(char)*4);
    }
    *returnSize = 1;
    strcpy(letter[0],"abc\0");
    strcpy(letter[1],"def\0");
    strcpy(letter[2],"ghi\0");
    strcpy(letter[3],"jkl\0");
    strcpy(letter[4],"mno\0");
    letter[i] = malloc(sizeof(char)*5);
    strcpy(letter[i++],"pqrs\0");
    letter[i] = malloc(sizeof(char)*4);
    strcpy(letter[i++],"tuv\0");
    letter[i] = malloc(sizeof(char)*5);
    strcpy(letter[i++],"wxyz\0");
    int len = strlen(digits);

    int lLen = strlen(letter[digits[0]-'0'-2]);
    char** send = malloc(sizeof(char*)*lLen);
    for(i = 0; i < lLen; i++)
    {
        send[i] = malloc(sizeof(char));
        send[i][0] = letter[digits[0]-'0'-2][i];
    }
    int size = lLen;
    *returnSize = size;
    if(len == 1)
    {
        for(i = 0; i < size; i++)
        {
            send[i][1] = '\0';
        }
        return send;
    }
    for(i = 1; i < len; i++)
    {
        send = make(send,&size,letter[digits[i]-'0'-2],i);
    }
    *returnSize = size;
    int j = 0;
    for(j = 0; j < size; j++)
    {
        send[j][i] = '\0';
    }
    return send;
}
char** make(char** input1, int* size, char* input2, int row)
{
    int i = 0;
    int j = 0;
    int k = 0;
    int count = 0;
    char** result = malloc(sizeof(char*)*(*size)*strlen(input2));
    for(i = 0; i < *size*strlen(input2); i++)
    {
        result[i] = malloc(sizeof(char)*(row+1));
    }
    for(i = 0; i < *size; i++)
    {
        for(j = 0; j < strlen(input2); j++)
        {
            for(k = 0; k < row; k++)
            {
                result[count][k] = input1[i][k];
            }
            count++;
        }
    }
    count = 0;
    for(i = 0; i < *size; i++)
    {
        for(j = 0; j < strlen(input2); j++)
        {
            result[count++][row] = input2[j];
        }
    }
    /*for(i = 0; i < count; i++)
    {
        for(j = 0; j < row+1; j++)
        {
            printf("%c ",result[i][j]);
        }
        printf("\n");
    }
    */
    for(i = 0; i < *size; i++)
    {
        free(input1[i]);
    }
    free(input1);
    *size = count;
    return result;
}

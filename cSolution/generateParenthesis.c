#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
char** generateParenthesis(int n, int* returnSize);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    int returnSize = 0;
    generateParenthesis(3,&returnSize);
    return 0;
}
void gen(char *stack, int top, int open, int close, char **p, int *siz)
{
	if (!open && !close) {
		printf("%s\n", stack);
		p[(*siz)++] = strdup(stack);
		return ;
	}

	if (open) {
		stack[top] = '(';
		gen(stack, top+1, open-1, close, p, siz);
	}

	if (close > open) {
		stack[top] = ')';
		gen(stack, top+1, open, close-1, p, siz);
	}
}

char** generateParenthesis(int n, int* returnSize) {
	char **p;
	char stack[n*2+1];

	
	stack[2*n] = '\0';
	*returnSize = 0;
	p = malloc(sizeof(char *) * 2000);
	gen(stack, 0, n, n, p, returnSize);

	return p;
}

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
struct ListNode* removeNthFromEnd(struct ListNode* head, int n);
struct ListNode {
    int val;
    struct ListNode *next;
};
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
void makeList(struct ListNode* head,int val)
{
    struct ListNode* temp = head;
    while(temp->next != NULL)
    {
        temp = temp->next;
    }
    struct ListNode *node = malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    temp->next = node;
}
int main()
{
    struct ListNode *head = malloc(sizeof(struct ListNode));
    head->val = 1;
    head->next = NULL;
    int i = 0;
    for(i = 2; i < 3; i++)
    {
        makeList(head,i);
    }
    struct ListNode *temp = head;
    while(temp != NULL)
    {
        printf("%d ",temp->val);
        temp = temp->next;
    }
    printf("\n");
    temp = removeNthFromEnd(head,2);
    while(temp != NULL)
    {
        printf("%d ",temp->val);
        temp = temp->next;
    }
    printf("\n");
    printf("\n");
    return 0;
}
struct ListNode* removeNthFromEnd(struct ListNode* head, int n)
{
    int count = 0;
    struct ListNode* temp = head;
    struct ListNode* tempVal = head;
    int val = head->val;
    while(temp != NULL)
    {
        if(count > n)
        {
            tempVal = tempVal->next;
        }
        temp = temp->next;
        count++;
    }
    if(count == 1 && n == 1) return NULL;
    if(count - n == 0)
    {
       temp = head;
       head = head->next;
       free(temp);
       return head;
    }
    if(tempVal != head || count - n == 1)
    {
        temp = tempVal->next;
        tempVal->next = tempVal->next->next;
        free(temp);
    }
    return head;
}

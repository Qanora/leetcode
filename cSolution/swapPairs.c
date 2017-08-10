#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)

int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
struct ListNode{
    int val;
    struct ListNode* next;
};
void add(struct ListNode* temp,int n);
void swap(struct ListNode* temp);
void display(struct ListNode* temp);
struct ListNode* swapPairs(struct ListNode* head);
int main()
{
    int i = 0;
    struct ListNode* head = malloc(sizeof(struct ListNode));
    struct ListNode* travel = head; 
    head->val = 0;
    head->next = NULL;
    for(i = 1; i < 1; i++)
    {
        add(travel,i);
        travel = travel->next;
    }
    display(head);
    travel = swapPairs(head);
    display(travel);
    return 0;
}
void add(struct ListNode* temp,int n)
{
    struct ListNode* node = malloc(sizeof(struct ListNode));
    node->val = n;
    node->next = NULL;
    temp->next = node;
}
void swap(struct ListNode* temp)
{
    struct ListNode* temp1 = temp;
    struct ListNode* temp2 = temp1->next;
    struct ListNode* temp3 = temp2->next;
    struct ListNode* temp4 = temp3->next;
    temp1->next = temp3;
    temp1->next->next = temp2;
    temp2->next = temp4;
}
void display(struct ListNode* temp)
{
    struct ListNode* travel = temp;
    while(travel != NULL)
    {
        printf("%d ",travel->val);
        travel = travel->next;
    }
    printf("\n");
}
struct ListNode* swapPairs(struct ListNode* head)
{
    struct ListNode* travel = malloc(sizeof(struct ListNode));
    travel->val = 0;
    travel->next = head;
    struct ListNode* temp = travel;
    while(travel != NULL && travel->next != NULL && travel->next->next != NULL)
    {
        swap(travel);
        travel = travel->next->next;
    }
    return temp->next;
}


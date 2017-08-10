#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<stdbool.h>
#define max(x,y) (x > y ? x : y)
#define min(x,y) (x < y ? x : y)
struct ListNode{
    int val;
    struct ListNode* next;
};
int nextList(struct ListNode* l1, struct ListNode* l2);
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2);
void add(struct ListNode* end, int val);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
void dispaly(struct ListNode* list)
{
    struct ListNode* temp = list;
    while(temp != NULL)
    {
        printf("%d ",temp->val);
        temp = temp->next;
    }
    printf("\n");
}
int main()
{
    int i = 0;
    struct ListNode* l1 = malloc(sizeof(struct ListNode));
    l1->val = 0;
    l1->next = NULL;
    struct ListNode* temp = l1;
    for(i = 0; i < 5; i++)
    {
        add(temp,i);
        temp = temp->next;
    }
    struct ListNode* l2 = malloc(sizeof(struct ListNode));
    l2->val = 0;
    l2->next = NULL;
    temp = l2;
    for(i = 2; i < 6; i++)
    {
        add(temp,i);
        temp = temp->next;
    }
    mergeTwoLists(l1->next,l2->next);
    dispaly(l1->next);
    dispaly(l2->next);
    return 0;
}
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
{
   struct ListNode* head = malloc(sizeof(struct ListNode));
   head->val = 0;
   head->next = NULL;
   struct ListNode* travel = head;
   struct ListNode* l1T = l1;
   struct ListNode* l2T = l2;
   int i = 0;
   int temp = 0;
   while(l1T != NULL && l2T != NULL)
   {
        if(l1T->val < l2T->val)
        {
            temp = l1T->val;
            l1T = l1T->next;
        }
        else
        {
            temp = l2T->val;
            l2T = l2T->next;
        }
        add(travel,temp);
        travel = travel->next;
   }
   while(l1T != NULL)
   {
       add(travel,l1T->val);
       travel = travel->next;
       l1T = l1T->next;
   }
   while(l2T != NULL)
   {
       add(travel,l2T->val);
       travel = travel->next;
       l2T = l2T->next;
   }
   dispaly(head->next);
}
void add(struct ListNode* end, int val)
{

    struct ListNode* node = malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    end->next = node;
}

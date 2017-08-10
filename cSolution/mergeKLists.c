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
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
void display(struct ListNode* list);
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize);
void add(struct ListNode* list,int n);
int main()
{
    struct ListNode** temp = malloc(sizeof(struct ListNode*)*2);
    struct ListNode* result1 = malloc(sizeof(struct ListNode));
    struct ListNode* result2 = malloc(sizeof(struct ListNode));
    struct ListNode* travel;
    result1->val = 0;
    result1->next = NULL;
    result2->val = 1;
    result2->next = NULL;
    temp[0] = result1;
    temp[1] = result2;
    travel = mergeKLists(temp,2);
    display(travel);
    return 0;
}
void display(struct ListNode* list)
{
    while(list != NULL)
    {
        printf("%d ",list->val);
        list = list->next;
    }
    printf("\n");
}
void add(struct ListNode* list,int n)
{
    struct ListNode* node = malloc(sizeof(struct ListNode));
    node->val = n;
    node->next = NULL;
    list->next = node;
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize)
{
    int i = 0;
    struct ListNode** cList = lists;
    int flag = 0;
    int j = 0;
    int k = 0;
    int min = INT_MAX;
    struct ListNode* head = malloc(sizeof(struct ListNode));
    struct ListNode* travel = head;
    head->val = 0;
    head->next = NULL;
    for(i = 0; i < listsSize; i++)
    {
        min = INT_MAX;
        flag = 0;
        for(k = 0; k < listsSize; k++)
        {
            if(cList[k] != NULL)
            {
                min = min(cList[k]->val,min);
                flag = 1;
            }
        }
        if(flag)
        {
            for(j = 0; j < listsSize; j++)
            {
                if(cList[j] != NULL)
                {
                    if(cList[j]->val == min)
                    {
                        add(travel,cList[j]->val);
                        travel = travel->next;
                        cList[j] = cList[j]->next;
                    }
                }
            }
        }
        if(i >= listsSize - 1 && flag)
        {
            i = -1;
        }
    }
    travel = head->next;
    free(head);
    return travel;
}

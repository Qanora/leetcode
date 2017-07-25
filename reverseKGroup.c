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
void display(struct ListNode* temp);
struct ListNode* reverseKGroup(struct ListNode* head, int k);
void add(struct ListNode* temp,int n);
struct ListNode* reverseKGroupD(struct ListNode* head, int k);
struct ListNode* reverse(struct ListNode* temp);
void swap(struct ListNode* temp);
struct ListNode* swapPairs(struct ListNode* head);
int cmpfunc(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
int main()
{
    struct ListNode* head = malloc(sizeof(struct ListNode));
    head->val = 0;
    head->next = NULL;
    struct ListNode* travel = head;
    int i = 0;
    for(i = 1; i < 12; i++)
    {
        add(travel,i);
        travel = travel->next;
    }
    display(head);
    head = reverseKGroup(head,3);
    display(head);
    return 0;
}
void add(struct ListNode* temp,int n)
{
    struct ListNode* node = malloc(sizeof(struct ListNode));
    node->val = n;
    node->next = NULL;
    temp->next = node;
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
struct ListNode* reverse(struct ListNode* temp)
{
    if(temp == NULL) return NULL;
    if(temp->next == NULL)
    {
        return temp;
    }
    else
    {
        struct ListNode* new = temp->next;
        //printf("new\n");
        //display(new);
        temp->next = NULL;
        struct ListNode* reNew = reverse(new);
        //printf("reNew\n");
        //display(reNew);
        new->next = temp; 
        //printf("new = %d, temp = %d\n",new->val,temp->val);
        return reNew;
    }
}

struct ListNode* reverseKGroup(struct ListNode* head, int k)
{
    if(head == NULL || head->next == NULL) return head;
    int count = 0;
    struct ListNode* travel = head;
    while(travel != NULL)
    {
        travel = travel->next;
        count++;
    }
    if(k == 1) return head;
    if(k == 2) return swapPairs(head);
    if(count < k) return head;
    if(count == k ) return reverse(head);
    return reverse(reverseKGroupD(head,k)); 
}
struct ListNode* reverseKGroupD(struct ListNode* head, int k)
{
    if(head == NULL) return NULL;
    struct ListNode* travel = head;
    int Tcount =0;
    //printf("lastHead->\n");
    //display(head);
    while(1)
    {
        if(Tcount > k - 2 && travel->next != NULL)
        {  
            break;
        }
        else if(travel->next != NULL)
        {
           travel = travel->next;
           Tcount++;
        }
        else if(travel->next != NULL || Tcount <= k - 2)
        {
            return reverse(head);
        }
        else
        {
            return head;
        }
    }
    struct ListNode* new;
    if(travel == NULL)
    {
        new = NULL;
    }
    else
    {
        new = travel->next;
        travel->next = NULL;
    }
    //printf("pre-new:\n");
    //display(new);
    struct ListNode* reNew = reverseKGroupD(new,k);
   // printf("reNew\n");
   // display(reNew);
   // printf("new\n");
   // display(new);
   // printf("head\n");
   // display(head);
    struct ListNode* Ttravel = new;
    if(Ttravel == NULL) return NULL;
    while(Ttravel->next != NULL)
    {
        Ttravel = Ttravel->next;
    }
    Ttravel->next =head;
    return reNew;
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



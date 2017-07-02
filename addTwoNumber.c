#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct ListNode* initialize();
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2);
struct ListNode* addTwoNumberss(struct ListNode* l1, struct ListNode* l2);


struct ListNode{
    int val;
    struct ListNode* next;
};

int main()
{
    struct ListNode* l1 = initialize(); 
    struct ListNode* l2 = initialize();
    l1->val = 1;
    l2->val = 2;
    struct ListNode* l4 = initialize();
    l4->val = 3;
    l1->next = l4;
    l2->next = l4;
    struct ListNode* l3 = addTwoNumberss(l1,l2);
    while(l1){
        printf("%d\n",l3->val);
        l3 = l3->next;
    }
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* head = initialize();
    struct ListNode* move = head;
    int extra = 0;
    while(l1 || l2)
    {
        move->val = (l1 ? l1->val: 0) + (l2 ? l2->val:0) + extra;
        extra = move->val / 10;
        move->val %= 10;
        l1 = l1? l1->next: NULL;
        l2 = l2? l2->next: NULL;
        if(l1 || l2 || extra ){
            struct ListNode* temp = initialize();
            temp->val = extra ? temp->val = 1: 0;
            move->next =temp;
            move = move->next;
        }
    }
    return head;
}

struct ListNode* initialize(){
    struct ListNode* point;
    point = (struct ListNode*)malloc(sizeof(struct ListNode*));
    point->next = NULL;
    point->val = 0;
    return point;
}


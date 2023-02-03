/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* NewList = malloc(sizeof(struct ListNode));\
    NewList->val = 0;
    NewList->next = NULL;
    int sum = 0;
    int remainder = 0;
    int one = 0;
    struct ListNode* temp = malloc(sizeof(struct ListNode));
    
    while (l1 != NULL && l2 != NULL)
    {
        sum = l1->val + l2->val + one;
        if (sum > 9)
        {
            remainder = sum % 10;
            one = 1;
        }
        else
        {
            remainder = sum;
            one = 0; 
        }
        struct ListNode* NewNode = malloc(sizeof(struct ListNode));
        NewNode->val = remainder;
        NewNode->next = NULL;
        temp = NewList;
        if (temp->next == NULL)
        {
            temp->next = NewNode;
        }
        else
        {      
            while (temp->next != NULL)
            {
                temp = temp->next;
            }
            temp->next = NewNode;
        }
        l1 = l1->next;
        l2 = l2->next;
     
    }
    return (NewList);
} 

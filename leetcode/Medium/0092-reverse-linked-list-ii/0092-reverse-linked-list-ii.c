/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right){
   struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
    temp->val = -1;
    temp->next = NULL;
    struct ListNode* prev = temp;
    prev->next = head;
        for(int i=0;i<left-1;i++)
            prev = prev->next;
        struct ListNode* cur = prev->next;
        for(int i=0;i<right-left;i++){
            struct ListNode* ptr = prev->next;
            prev->next=cur->next;
            cur->next = cur->next->next;
            prev->next->next=ptr;
        }
        return temp->next;
}
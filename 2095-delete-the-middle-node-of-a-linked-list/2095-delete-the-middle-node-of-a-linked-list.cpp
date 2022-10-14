/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

#include <iostream>

using namespace std;

class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        int length = getLength(head);
        int middle = 0;
        if(length % 2 == 0){
            middle = length/2;
        }else{
            middle = (length-1)/2;
        }
        
        ListNode* middleBefore = head;
        
        for(int i=0;i<middle - 1;i++){
            middleBefore = middleBefore->next;
        }
        
        if(head->next == NULL){
            head = nullptr;
        }else if(middleBefore -> next -> next != NULL){
            middleBefore -> next = middleBefore->next->next;
        }else{
            middleBefore->next = nullptr;
        }
        
        
        return head;
    }
    
    int getLength(ListNode* head){
        ListNode* node = head;
        int length = 1;
        while(node->next != NULL){
            length++;
            node = node->next;
        }
        return length;
    }
};
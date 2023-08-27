/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include <stddef.h>
#include <stdlib.h>
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if (list1 == NULL && list2 == NULL) {
        return NULL;
    }

    struct ListNode* answer = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* answerp = answer;
    struct ListNode* firstp = list1;
    struct ListNode* nextp = list2;

    while (1) {
        int a = -101;
        int b = -101;

        if (firstp != NULL) {
            a = firstp->val;
        }
        if (nextp != NULL) {
            b = nextp->val;
        }

        if ((a >= b && b > -101) || (a == -101 && b > -101)) {
            answerp->val = b;
            nextp = nextp->next;
        } else if ((a < b && a > -101) || (a > -101 && b == -101)) {
            answerp->val = a;
            firstp = firstp->next;
        }

        if (firstp == NULL && nextp == NULL) {
            answerp->next = NULL;
            break;
        } else {
            answerp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            answerp = answerp->next;
        }
    }

    return answer;
}
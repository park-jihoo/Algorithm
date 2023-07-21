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
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
    if (list1 == NULL && list2 == NULL) {
      return nullptr;
    }
    ListNode *answer = new ListNode();
    ListNode *answerp = answer;
    ListNode *firstp = list1;
    ListNode *nextp = list2;
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
        break;
      } else {
        answerp->next = new ListNode();
        answerp = answerp->next;
      }
    }
    return answer;
  }
};
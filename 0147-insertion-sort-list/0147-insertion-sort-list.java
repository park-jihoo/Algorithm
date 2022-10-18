/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {ListNode sorted = new ListNode(head.val);
        ListNode now = head.next;
        if (now == null)
            return sorted;

        ListNode answer = sorted;
        while (now != null) {
            ListNode point = answer;
            boolean flag = false;
            while (point != null) {
                if (now.val >= point.val && (point.next == null || now.val < point.next.val)) {
                    point.next = new ListNode(now.val, point.next);
                    flag = true;
                    break;
                } else
                    point = point.next;
            }
            if (!flag) {
                answer = new ListNode(now.val, answer);
            }
            now = now.next;
        }
        return answer;
    }
}
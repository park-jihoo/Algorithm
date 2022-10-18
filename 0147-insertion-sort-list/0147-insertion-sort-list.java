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
    public ListNode insertionSortList(ListNode head) {
        ListNode sorted = new ListNode(head.val);
        ListNode now = head.next;
        if(now == null)
            return sorted;

        ListNode answer = sorted;
        while(now != null){
            ListNode point = answer;
            boolean flag = false;
            while(point != null){
                if(now.val >= point.val && (point.next==null || point.next != null && now.val < point.next.val)){
                    ListNode insert = new ListNode(now.val, point.next);
                    point.next = insert;
                    flag = true;
                    break;
                }else
                    point = point.next;
            }
            if(!flag){
                ListNode insert = new ListNode(now.val, answer);
                answer = insert;
            }
            now = now.next;
        }
        return answer;
    }
}
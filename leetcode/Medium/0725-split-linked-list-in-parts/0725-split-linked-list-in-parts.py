# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        wid, rem = divmod(length, k)
        answer = []
        curr = head
        for i in range(k):
            head = write = ListNode(None)
            for j in range(wid + (i < rem)):
                write.next = write = ListNode(curr.val)
                if curr:
                    curr = curr.next
            answer.append(head.next)
        return answer

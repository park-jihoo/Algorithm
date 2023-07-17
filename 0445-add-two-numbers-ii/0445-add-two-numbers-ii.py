# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q1, q2 = deque(), deque()
        while l1:
            q1.append(l1.val)
            l1 = l1.next
        while l2:
            q2.append(l2.val)
            l2 = l2.next
        
        q3 = deque()
        temp = 0
        while q1 or q2:
            if q1:
                temp+=q1.pop()
            if q2:
                temp+=q2.pop()
            if temp >= 10:
                q3.append(temp - 10)
                temp = 1
            else:
                q3.append(temp)
                temp = 0
        if temp == 1:
            q3.append(temp)
        answer = ListNode(q3.popleft())
        while q3:
            answer = ListNode(q3.popleft(), answer)

        return answer
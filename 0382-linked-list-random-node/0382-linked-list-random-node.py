import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        now = self.head
        while now is not None:
            self.length+=1
            now = now.next

    def getRandom(self) -> int:
        idx = random.randrange(0, self.length)
        rand = self.head
        for i in range(idx):
            rand = rand.next
        return rand.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
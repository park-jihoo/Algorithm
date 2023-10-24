# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        answer = []
        q = deque([root])
        while q:
            length = len(q)
            maximum = float("-inf")

            for i in range(length):
                node = q.popleft()
                maximum = max(maximum, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            answer.append(maximum)
        return answer

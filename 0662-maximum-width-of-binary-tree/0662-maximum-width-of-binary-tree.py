from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        answer = 1
        cur = deque([(root, 1)])
        nex = deque([])
        while cur:
            node, pos = cur.popleft()
            if node.left is not None:
                nex.append((node.left, pos * 2))
            if node.right is not None:
                nex.append((node.right, pos * 2 + 1))
            if len(cur) == 0 and len(nex) > 0:
                cur, nex = nex, cur
                answer = max(answer, cur[len(cur) - 1][1] - cur[0][1] + 1)

        return answer

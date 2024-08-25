# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left -> right -> parent
        answer = []
        if not root:
            return []
        stack = deque([])
        curr = root
        while curr or stack:
            if curr:
                answer.append(curr.val)
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                curr = curr.left
        answer.reverse()
        return answer

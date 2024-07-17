# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = [root] if root.val not in to_delete else []
        # dfs
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                stack.append(node.right)
                if node.right.val in to_delete:
                    node.right = None
            if node.val in to_delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
        return ans
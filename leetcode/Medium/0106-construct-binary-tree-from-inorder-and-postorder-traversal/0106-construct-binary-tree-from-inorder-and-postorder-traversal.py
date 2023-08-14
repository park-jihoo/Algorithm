# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeFunc(self, inorder, postorder, start, end):
        if start > end:
            return None
        cur = postorder[self.idx]
        node = TreeNode(cur)
        self.idx -= 1

        if start == end:
            return node
        inIdx = self.d[cur]
        node.right = self.buildTreeFunc(inorder, postorder, inIdx + 1, end)
        node.left = self.buildTreeFunc(inorder, postorder, start, inIdx - 1)
        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        self.d, self.idx = {}, 0
        for i in range(n):
            self.d[inorder[i]] = i
        self.idx = n - 1
        return self.buildTreeFunc(inorder, postorder, 0, n - 1)

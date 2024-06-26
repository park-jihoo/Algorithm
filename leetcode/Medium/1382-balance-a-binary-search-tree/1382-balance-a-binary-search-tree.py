# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def arrBST(self, arr):
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return TreeNode(val=arr[0])
        mid = len(arr) // 2
        root = TreeNode(val=arr[mid])
        root.left = self.arrBST(arr[:mid])
        root.right = self.arrBST(arr[mid + 1 :])
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = self.inorder(root)
        return self.arrBST(arr)

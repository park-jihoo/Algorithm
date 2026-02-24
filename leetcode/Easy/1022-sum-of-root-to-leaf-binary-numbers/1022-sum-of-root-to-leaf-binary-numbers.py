# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        curr = 0
        node = root

        while node:
            if not node.left:
                curr = (curr << 1) | node.val
                if not node.right:
                    total += curr
                node = node.right
            else:
                prev = node.left
                steps = 1

                while prev.right and prev.right is not node:
                    prev = prev.right
                    steps += 1

                if not prev.right:
                    curr = (curr << 1) | node.val
                    prev.right = node
                    node = node.left
                else:
                    if not prev.left:
                        total += curr
                    prev.right = None
                    curr >>= steps
                    node = node.right
        return total

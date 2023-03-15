# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = [root]
        flag = False
        while q:
            temp = q.pop(0)
            if temp is None:
                flag = True
            else:
                if flag:
                    return False
                q.append(temp.left)
                q.append(temp.right)

        return True
            
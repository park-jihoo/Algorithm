# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleBST(self, start, end, memo):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[(start, end)]
        
        for i in range(start, end + 1):
            left = self.allPossibleBST(start, i - 1, memo)
            right = self.allPossibleBST(i + 1, end, memo)
            
            for l in left:
                for r in right:
                    root = TreeNode(i, l, r)
                    res.append(root)
        
        memo[(start, end)] = res
        return res
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.allPossibleBST(1, n, memo)
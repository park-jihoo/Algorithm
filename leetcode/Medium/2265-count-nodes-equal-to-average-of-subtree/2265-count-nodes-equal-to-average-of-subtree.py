# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return [0, 0]

            lSum, lCnt = dfs(root.left)
            rSum, rCnt = dfs(root.right)

            nodeSum = lSum + rSum + root.val
            nodeCnt = lCnt + rCnt + 1

            if nodeSum // nodeCnt == root.val:
                ans += 1
            return [nodeSum, nodeCnt]

        dfs(root)
        return ans

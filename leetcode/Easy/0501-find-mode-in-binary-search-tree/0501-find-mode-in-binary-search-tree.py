# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = defaultdict(int)

    def dfs(self, node):
        if not node:
            return
        self.counter[node.val] += 1
        self.dfs(node.left)
        self.dfs(node.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        freq = max(self.counter.values())
        ans = []
        for key in self.counter:
            if self.counter[key] == freq:
                ans.append(key)
        return ans

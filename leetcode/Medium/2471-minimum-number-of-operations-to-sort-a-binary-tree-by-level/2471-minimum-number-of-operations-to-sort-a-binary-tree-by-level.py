# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            size = len(q)
            lvl = [node.val for node in q]
            arr = sorted(lvl)
            d = {arr[i]:i for i in range(size)}
            for i in range(size):
                j = d[lvl[i]]
                while i!=j:
                    ans += 1
                    lvl[i],lvl[j],j=lvl[j],lvl[i],d[lvl[j]]
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
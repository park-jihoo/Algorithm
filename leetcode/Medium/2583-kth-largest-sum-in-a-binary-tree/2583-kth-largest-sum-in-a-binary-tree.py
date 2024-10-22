# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        queue = deque([])
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            if len(sums) < level + 1:
                sums.append(0)
            sums[level] -= node.val
        heapq.heapify(sums)
        if k > len(sums):
            return -1
        for i in range(k):
            ans = heapq.heappop(sums)
        return -ans

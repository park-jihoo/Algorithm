# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_distance = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # root에서의 거리 + 가장 깊은 노드까지의 거리 혹은 leaf까지의 거리
        self.traverse(root, start)
        return self.max_distance
    
    def traverse(self, root, start):
        depth = 0
        if root is None:
            return depth
        left = self.traverse(root.left, start)
        right = self.traverse(root.right, start)

        if root.val == start:
            self.max_distance = max(left, right)
            depth = -1
        elif left >= 0 and right >= 0:
            depth = max(left, right) + 1
        else:
            dist = abs(left) + abs(right)
            self.max_distance = max(self.max_distance, dist)
            depth = min(left, right) - 1
        return depth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # same depth with different parents
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
            sums[level] += node.val
        
        queue.append((root, 0, 0))
        while queue:
            node, sib, level = queue.popleft()
            if node.left and node.right:
                queue.append((node.left, node.right.val, level + 1))
                queue.append((node.right, node.left.val, level + 1))
            elif node.left:
                queue.append((node.left, 0, level + 1))
            elif node.right:
                queue.append((node.right, 0, level + 1))
            node.val = sums[level] - node.val - sib
        return root
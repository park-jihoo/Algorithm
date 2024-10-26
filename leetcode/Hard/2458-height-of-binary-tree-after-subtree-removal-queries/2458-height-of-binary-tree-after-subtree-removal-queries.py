# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        @lru_cache(None)
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        d = defaultdict(int)

        stack = [(root, 0, 0)]

        while stack:
            node, depth, maxval = stack.pop()
            if node:
                d[node.val] = maxval
                stack.append(
                    (node.right, depth + 1, max(maxval, depth + 1 + height(node.left)))
                )
                stack.append(
                    (node.left, depth + 1, max(maxval, depth + 1 + height(node.right)))
                )

        return [d[i] for i in queries]

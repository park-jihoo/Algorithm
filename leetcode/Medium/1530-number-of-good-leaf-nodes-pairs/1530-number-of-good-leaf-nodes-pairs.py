# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaves = []
        graph = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                graph[node.left].append(node)
                graph[node].append(node.left)
            if node.right:
                stack.append(node.right)
                graph[node.right].append(node)
                graph[node].append(node.right)
            if not node.left and not node.right:
                leaves.append(node)
        ans = 0
        for leaf in leaves:
            q = deque([(leaf, 0)])
            seen = set(q)
            while q:
                node, length = q.popleft()
                if length > distance:
                    break
                if node:
                    for nbr in graph[node]:
                        if nbr not in seen:
                            seen.add(nbr)
                            q.append((nbr, length + 1))
                    if node != leaf and not node.left and not node.right:
                        ans += 1

        return ans // 2

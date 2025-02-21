# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        q = deque([root])
        self.set = set([])
        while q:
            node = q.popleft()
            self.set.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                q.append(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                q.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
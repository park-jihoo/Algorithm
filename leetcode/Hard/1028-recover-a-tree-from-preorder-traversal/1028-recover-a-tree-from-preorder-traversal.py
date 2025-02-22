# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        pattern = "[0-9]+|[-]+"
        tokens = re.findall(pattern, traversal)

        root = TreeNode(int(tokens[0]))
        node_lvl = {0: root}

        for i in range(1, len(tokens), 2):

            depth = len(tokens[i])
            node = TreeNode(int(tokens[i + 1]))
            parent = node_lvl[depth - 1]

            if parent.left is None:
                parent.left = node
            else:
                parent.right = node

            node_lvl[depth] = node

        return root

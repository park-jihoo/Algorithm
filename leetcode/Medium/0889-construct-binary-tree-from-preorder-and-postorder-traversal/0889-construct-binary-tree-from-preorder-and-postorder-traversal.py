# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        graph = {}
        for val in preorder:
            graph[val] = TreeNode(val)
        while postorder:
            node = postorder[0]
            idx = preorder.index(node)
            parent = preorder[idx - 1]
            if idx - 1 < 0:
                return graph[node]
            if not graph[parent].left:
                graph[parent].left = graph[node]
            else:
                graph[parent].right = graph[node]

            postorder = postorder[1:]
            preorder = preorder[:idx] + preorder[idx + 1 :]

        return graph[node]

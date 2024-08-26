"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        answer = []
        if root == None:
            return answer

        stack = deque([root])
        while stack:
            curr = stack.pop()
            answer.append(curr.val)
            stack.extend(curr.children)

        return answer[::-1]

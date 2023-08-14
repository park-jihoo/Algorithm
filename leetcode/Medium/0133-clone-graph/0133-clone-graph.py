"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None
        q = deque([node])
        nodes = {node.val: Node(node.val)}
        while q:
            n = q.popleft()
            cur = nodes[n.val]
            for neighbor in n.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                cur.neighbors.append(nodes[neighbor.val])
        return nodes[node.val]

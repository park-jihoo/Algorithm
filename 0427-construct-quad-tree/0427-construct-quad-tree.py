"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def same(length, rs, cs):
            value = grid[rs][cs]
            for i in range(rs, rs+length):
                for j in range(cs, cs+length):
                    if value != grid[i][j]:
                        return False
            return True
        def tree(length, rs, cs):
            node = Node(False, False, None, None, None, None)
            if same(length, rs, cs):
                node.val = grid[rs][cs]
                node.isLeaf = True
            elif length != 1:
                node.val = True
                node.isLeaf = False
                node.topLeft = tree(length // 2, rs, cs)
                node.topRight = tree(length // 2, rs, cs + length // 2)                
                node.bottomLeft = tree(length // 2, rs + length // 2, cs)                
                node.bottomRight = tree(length // 2, rs + length // 2, cs + length // 2)
            else:
                node.val = grid[rs][cs]
                node.isLeaf = True
            return node
        return tree(len(grid), 0, 0)
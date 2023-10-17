class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        
        root = find_root()
        if root == -1:
            return False
        
        # dfs
        visited = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1 and child in visited:
                    return False
                elif child != -1:
                    stack.append(child)
                    visited.add(child)

        return len(visited) == n
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Array/Hash Table/String/BFS
        graph = {str(x): [str(x + 9)[-1], str(x + 1)[-1]] for x in range(10)}
        visit = set(deadends)
        queue = deque([["0000", 0]])
        while queue:
            node, dist = queue.popleft()
            if node == target:
                return dist
            numlist = list(node)
            if node not in visit:
                visit.add(node)
                for idx, num in enumerate(numlist):
                    for n in graph[num]:
                        newnode = numlist[:]
                        newnode[idx] = n
                        queue.append(["".join(newnode), dist + 1])

        return -1

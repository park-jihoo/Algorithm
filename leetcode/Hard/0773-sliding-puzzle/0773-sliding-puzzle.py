class Solution:
    def swap(self, char, idx1, idx2):
        lch = list(char)
        lch[idx1], lch[idx2] = lch[idx2], lch[idx1]
        return "".join(lch)

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 6! = 720
        graph = defaultdict(list)
        initial = ("123450", 5, 0)
        queue = deque([initial])
        visited = set()
        target = "".join(list(map(str, board[0]))) + "".join(list(map(str, board[1])))
        while queue:
            node, pos, dist = queue.popleft()
            if node == target:
                return dist
            if node not in visited:
                visited.add(node)
                if pos % 3 != 2:
                    queue.append((self.swap(node, pos, pos + 1), pos + 1, dist + 1))
                if pos % 3 != 0:
                    queue.append((self.swap(node, pos, pos - 1), pos - 1, dist + 1))
                queue.append(
                    (self.swap(node, pos, (pos + 3) % 6), (pos + 3) % 6, dist + 1)
                )
        return -1

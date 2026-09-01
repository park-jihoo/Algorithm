class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        L = {
            (r, c): 1 << i
            for i, (r, c) in enumerate(
                (r, c)
                for r, row in enumerate(classroom)
                for c, v in enumerate(row)
                if v == "L"
            )
        }
        S = next(
            (r, c)
            for r, row in enumerate(classroom)
            for c, v in enumerate(row)
            if v == "S"
        )

        target = (1 << len(L)) - 1
        if not target:
            return 0

        q, steps = deque([(*S, 0, energy)]), 0
        V = {(*S, 0): energy}

        while q:
            for _ in range(len(q)):
                r, c, m, e = q.popleft()
                if e < V.get((r, c, m), -1) or e == 0:
                    continue

                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < len(classroom)
                        and 0 <= nc < len(classroom[0])
                        and classroom[nr][nc] != "X"
                    ):
                        nm = m | L.get((nr, nc), 0)
                        if nm == target:
                            return steps + 1

                        ne = energy if classroom[nr][nc] == "R" else e - 1
                        if ne > V.get((nr, nc, nm), -1):
                            V[nr, nc, nm] = ne
                            q.append((nr, nc, nm, ne))
            steps += 1

        return -1

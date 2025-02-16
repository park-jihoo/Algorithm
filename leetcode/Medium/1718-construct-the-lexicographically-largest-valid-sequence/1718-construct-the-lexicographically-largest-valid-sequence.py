class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        sequence = [0] * size
        used = [False] * (n + 1)

        def backtrack(pos):
            if pos == size:
                return True
            if sequence[pos] != 0:
                return backtrack(pos + 1)
            for num in range(n, 1, -1):
                if not used[num] and pos + num < size and sequence[pos + num] == 0:
                    sequence[pos] = sequence[pos + num] = num
                    used[num] = True
                    if backtrack(pos + 1):
                        return True
                    sequence[pos] = sequence[pos + num] = 0
                    used[num] = False

            if not used[1]:
                sequence[pos] = 1
                used[1] = True
                if backtrack(pos + 1):
                    return True
                sequence[pos] = 0
                used[1] = False
            return False

        backtrack(0)
        return sequence

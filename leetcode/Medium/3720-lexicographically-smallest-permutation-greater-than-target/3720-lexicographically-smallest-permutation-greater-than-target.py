class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)

        for i in range(len(target) - 1, -1, -1):
            used = Counter(target[:i])
            if any(used[c] > cnt[c] for c in used):
                continue

            available = cnt - used
            bigger = min((c for c in available if c > target[i]), default=None)

            if bigger:
                available[bigger] -= 1
                return target[:i] + bigger + ''.join(
                    c * available[c] for c in sorted(available)
                )

        return ""
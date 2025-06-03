class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(status)
        can_open = [status[i] for i in range(n)]
        has_box, used = [False] * n, [False] * n

        q = deque([])
        ans = 0
        for box in initialBoxes:
            has_box[box] = True
            if can_open[box]:
                q.append(box)
                used[box] = True
                ans += candies[box]

        while q:
            big_box = q.popleft()
            for key in keys[big_box]:
                can_open[key] = True
                if not used[key] and has_box[key]:
                    q.append(key)
                    used[key] = True
                    ans += candies[key]
            for box in containedBoxes[big_box]:
                has_box[box] = True
                if not used[box] and can_open[box]:
                    q.append(box)
                    used[box] = True
                    ans += candies[box]

        return ans

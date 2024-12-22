class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        ans, indices = [0] * len(queries), []
        for idx, query in enumerate(queries):
            left, right = sorted(query)
            if left == right or heights[left] < heights[right]:
                ans[idx] = right
            else:
                indices.append((left, right, idx))
        j, stack = len(heights) - 1, deque()
        for left, right, idx in sorted(indices, key=lambda x: x[1], reverse=True):
            while j > right:
                while stack and heights[stack[0]] < heights[j]:
                    stack.popleft()
                stack.appendleft(j)
                j -= 1
            k = bisect_right(stack, heights[left], key=lambda x: heights[x])
            ans[idx] = -1 if k == len(stack) else stack[k]
        return ans

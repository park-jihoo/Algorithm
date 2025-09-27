class Solution:
    def area(self, a, b, c):
        return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1]-a[1]) + c[0] * (a[1]-b[1])) / 2

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    ans = max(ans, self.area(points[i], points[j], points[k]))
        return ans
        
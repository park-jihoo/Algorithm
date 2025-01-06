class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        boxes = list(map(int, boxes))
        answer = [0] * n

        for i in range(n):
            answer[i] += sum(accumulate(boxes[:i], initial=0))
        for i in range(n - 1, -1, -1):
            answer[i] += sum(accumulate(boxes[n - 1 : i : -1], initial=0))

        return answer

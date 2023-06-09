class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        while start <= end:
            mid = (start + end) // 2
            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return letters[start % len(letters)]
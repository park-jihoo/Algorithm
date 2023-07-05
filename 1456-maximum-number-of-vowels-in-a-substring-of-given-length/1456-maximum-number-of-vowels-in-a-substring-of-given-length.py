class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        count = Counter(s[:k])
        answer = 0
        answer += count.get('a') if count.get('a') is not None else 0
        answer += count.get('e') if count.get('e') is not None else 0
        answer += count.get('i') if count.get('i') is not None else 0
        answer += count.get('o') if count.get('o') is not None else 0
        answer += count.get('u') if count.get('u') is not None else 0
        vowels = answer
        for i in range(1, n - k + 1):
            if s[i-1] in ['a', 'e', 'i', 'o', 'u']:
                vowels -= 1
            if s[i+k - 1] in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
            answer = max(vowels, answer)
        return answer
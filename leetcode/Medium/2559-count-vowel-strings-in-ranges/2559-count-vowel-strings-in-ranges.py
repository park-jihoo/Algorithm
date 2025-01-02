class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        vowel_string = [int(word[0] in vowels and word[-1] in vowels) for word in words]
        pref = [0]+list(accumulate(vowel_string))
        return [pref[y+1]-pref[x] for x, y in queries]
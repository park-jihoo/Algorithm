class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in anagram_groups:
                anagram_groups[s_sorted].append(s)
            else:
                anagram_groups[s_sorted] = [s]
        return list(anagram_groups.values())

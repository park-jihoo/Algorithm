class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_sets = [set(l) for l in languages]

        to_fix = set()
        for a, b in friendships:
            if lang_sets[a-1].isdisjoint(lang_sets[b-1]):
                to_fix.add(a-1)
                to_fix.add(b-1)

        if not to_fix:
            return 0
            
        count = defaultdict(int)
        for person in to_fix:
            for lang in range(1, n+1):
                if lang not in lang_sets[person]:
                    count[lang] += 1

        return min(count.values())
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ppl = sorted(
            [(names[i], heights[i]) for i in range(len(names))], key=lambda x: -x[1]
        )
        return [x[0] for x in ppl]

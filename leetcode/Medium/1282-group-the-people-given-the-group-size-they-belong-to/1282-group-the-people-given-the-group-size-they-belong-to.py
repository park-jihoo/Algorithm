class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []

        for idx, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(idx)

            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(list)
        for x, y in adjacentPairs:
            adj_dict[x].append(y)
            adj_dict[y].append(x)

        ans = []
        for key, value in adj_dict.items():
            if len(value) == 1:
                ans.extend([key, value[0]])
                break
        for i in range(len(adjacentPairs)):
            can = adj_dict[ans[-1]]
            if len(can) == 1:
                break
            elif can[0] == ans[-2]:
                ans.append(can[1])
            else:
                ans.append(can[0])
        return ans

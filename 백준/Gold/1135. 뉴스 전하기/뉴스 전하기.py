from collections import defaultdict

N = int(input())
people = list(map(int, input().split()))

people_map = defaultdict(list)

for i in range(1, N):
    people_map[people[i]].append(i)

dp = [0 for i in range(N)]


def dfs(here):
    temp = []
    for ppl in people_map[here]:
        dfs(ppl)
        temp.append(dp[ppl])
    if temp:
        temp.sort(reverse=True)
        next_time = [temp[i] + i + 1 for i in range(len(temp))]
        dp[here] = max(next_time)


dfs(0)
print(dp[0])

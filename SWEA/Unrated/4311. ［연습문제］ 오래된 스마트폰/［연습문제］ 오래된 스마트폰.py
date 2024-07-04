from collections import deque


def cal(num1, num2, oper):
    ans = 0
    if oper == 1:
        ans = num1 + num2
    elif oper == 2:
        ans = num1 - num2
    elif oper == 3:
        ans = num1 * num2
    elif num2 == 0:
        return -1
    else:
        ans = num1 // num2
    if ans < 0 or ans > 999:
        return -1
    return ans


def recur(cur, x):
    if cur == 3:
        return
    for num in nums:
        nxt_num = x * 10 + num
        if visited[nxt_num] <= cur + 1:
            continue
        visited[nxt_num] = cur + 1
        q.append(nxt_num)
        ns.append(nxt_num)
        recur(cur + 1, nxt_num)


t = int(input())

for test_case in range(1, t + 1):
    n, o, m = map(int, input().split())
    nums = list(map(int, input().split()))
    operations = list(map(int, input().split()))  # 1: +, 2: -, 3: *, 4: /
    ns = []
    w = int(input())
    # 중간값: 0~999

    # can use numbers several times
    # can use operations several times

    # find minimum touch count to make w
    # if it is impossible, return -1
    visited = [m + 1] * 1000
    q = deque()
    recur(0, 0)

    if visited[w] < m:
        print(f"#{test_case} {visited[w]}")
        continue

    while q:
        val = q.popleft()
        for num in ns:
            clicks = visited[val] + len(str(num)) + 1
            if clicks + 1 > m:
                continue
            for oper in operations:
                nxt = cal(val, num, oper)
                if nxt == -1:
                    continue
                if visited[nxt] <= clicks:
                    continue
                visited[nxt] = clicks
                q.append(nxt)

    if visited[w] >= m:
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {visited[w]+1}")

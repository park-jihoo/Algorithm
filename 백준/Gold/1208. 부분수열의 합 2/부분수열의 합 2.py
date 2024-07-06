# acmicpc.net/problem/1208
# 부분수열의 합 2

from bisect import bisect_left, bisect_right

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = arr[: n // 2], arr[n // 2 :]
left_sum, right_sum = [], []


def get_sum(arr, sum_arr, x, start):
    for i in range(start + 1, len(arr)):
        sum_arr.append(x + arr[i])
        get_sum(arr, sum_arr, x + arr[i], i)


get_sum(left, left_sum, 0, -1)
get_sum(right, right_sum, 0, -1)

left_sum.append(0)
right_sum.append(0)

left_sum.sort()
right_sum.sort()

answer = 0
for x in left_sum:
    answer += bisect_right(right_sum, s - x) - bisect_left(right_sum, s - x)

if s == 0:
    answer -= 1

print(answer)

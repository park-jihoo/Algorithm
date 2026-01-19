# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
"""
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
"""

# 표준 출력 예제
"""
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
"""

import sys

"""
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
"""

from collections import defaultdict

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())

seat = [[0] * N for x in range(N)]

likedict = defaultdict(list)

result = 0

for _ in range(N * N):
    inputt = list(map(int, input().split()))
    likedict[inputt[0]] = inputt[1:]

    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                likecnt = 0
                emptycnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if seat[nx][ny] in inputt:
                            likecnt += 1
                        if seat[nx][ny] == 0:
                            emptycnt += 1
                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    max_x, max_y, max_like, max_empty = i, j, likecnt, emptycnt

    seat[max_x][max_y] = inputt[0]


for i in range(N):
    for j in range(N):
        cnt = 0
        like = likedict[seat[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] in like:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)

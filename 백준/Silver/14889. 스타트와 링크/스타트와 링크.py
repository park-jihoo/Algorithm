n = int(input())

ability = [[int(x) for x in input().split()] for i in range(n)]

start, link = [], []

answer = []

def divide(idx):
    if (idx == n+1):
        if(len(start) == len(link) and len(start) == n // 2):
            start_sum = 0
            link_sum = 0
            for i in range(n//2):
                for j in range(i+1, n//2):
                    if i==j:
                        continue
                    start1, start2, link1, link2 = start[i]-1, start[j]-1, link[i]-1, link[j]-1
                    start_sum += ability[start1][start2]+ability[start2][start1]
                    link_sum += ability[link1][link2]+ability[link2][link1]

            answer.append(abs(start_sum - link_sum))
        return

    start.append(idx)
    divide(idx+1)
    start.pop()

    link.append(idx)
    divide(idx+1)
    link.pop()

divide(1)
print(min(answer))
A, B, C = sorted(list(map(int, input().split())))

order = list(input())

answer = []

for o in order:
    if o == "A":
        answer.append(str(A))
    elif o == "B":
        answer.append(str(B))
    else:
        answer.append(str(C))

print(" ".join(answer))
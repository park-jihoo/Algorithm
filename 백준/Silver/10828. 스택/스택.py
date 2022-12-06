import sys

N = int(sys.stdin.readline())
q = []

for i in range(N):
    x = sys.stdin.readline().split()
    if len(x) == 2:
        q.append(int(x[1]))
    elif x[0] == "pop":
        if q:
            print(q.pop(-1))
        else:
            print("-1")
    elif x[0] == "size":
        print(len(q))
    elif x[0] == "empty":
        print(int(len(q) == 0))
    elif x[0] == 'top':
        if q:
            print(q[-1])
        else:
            print("-1")
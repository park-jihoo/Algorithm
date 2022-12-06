import sys

n = int(input())
a = list(input())
for i in range(n-1):
    b = list(input())
    for j in range(len(a)):
        if a[j] != b[j]:
            a[j] = '?'

print(''.join(a))
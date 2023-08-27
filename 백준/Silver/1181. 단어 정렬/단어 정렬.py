N = int(input())
words = list(set([input() for x in range(N)]))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)

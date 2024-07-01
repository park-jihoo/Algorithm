T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    boxes = [sorted(list(map(int, input().split()))) for _ in range(N)]
    B = []
    for i, box in enumerate(boxes):
        B.append((box[0], box[1], box[2], i))
        B.append((box[0], box[2], box[1], i))
        B.append((box[1], box[2], box[0], i))

    B = sorted(B, key=lambda x: x[0] * x[1])

    dp = [b[2] for b in B]
    hist = [[b[3]] for b in B]

    for i in range(len(B)):
        for j in range(i):
            upper, lower = B[j], B[i]
            if lower[3] in hist[j]:
                continue
            if upper[0] > lower[0] or upper[1] > lower[1]:
                continue
            if dp[j] + lower[2] >= dp[i]:
                dp[i] = dp[j] + lower[2]
                hist[i] = hist[j] + [lower[3]]

    max_height = max(dp)
    print(f'#{test_case} {max_height}')
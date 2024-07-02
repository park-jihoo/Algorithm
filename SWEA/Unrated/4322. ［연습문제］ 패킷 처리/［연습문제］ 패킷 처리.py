T = int(input())


def dfs(idx, num_cpu, time):
    global cpu
    receive_time, len_packet = packets[idx]
    time_diff = receive_time - time

    for i in range(num_cpu):
        cpu[i] = max(cpu[i] - time_diff, 0)

    key = tuple([idx] + sorted(cpu))
    if key in memory:
        return False
    memory.add(key)

    for i in range(num_cpu):
        if cpu[i] + len_packet <= 10:
            if idx < n - 1:
                tmp = cpu[:]
                cpu[i] += len_packet
                if dfs(idx + 1, num_cpu, receive_time):
                    return True
                cpu = tmp
            else:
                return True
    return False


for test_case in range(1, T + 1):
    n = int(input())
    packets = [list(map(int, input().split())) for _ in range(n)]
    ans = -1
    for num_cpu in range(1, 6):
        cpu = [0] * num_cpu
        memory = set()
        if dfs(0, num_cpu, 0):
            ans = num_cpu
            break
    print(f"#{test_case} {ans}")
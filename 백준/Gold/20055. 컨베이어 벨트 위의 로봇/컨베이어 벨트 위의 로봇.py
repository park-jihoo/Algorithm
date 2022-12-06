from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
time = 0
robot = deque([0] * N)

while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(N - 2, -1, -1):
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
        robot[-1] = 0
    if robot[0] == 0 and belt[0] >=1:
        robot[0] = 1
        belt[0] -=1
    time +=1
    if belt.count(0) >= K:
        break
print(time)

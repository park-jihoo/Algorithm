class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack

    def asteroidCollision2(self, asteroids: List[int]) -> List[int]:
        # Array Stack Simulation
        passed = False
        while not passed:
            q = deque()
            for idx, val in enumerate(asteroids):
                if not q:
                    q.append(val)
                else:
                    left = q.pop()
                    if left > 0 and val < 0:
                        if left + val == 0:
                            continue
                        elif left + val > 0:
                            q.append(left)
                        else:
                            q.append(val)
                    else:
                        q.append(left)
                        q.append(val)
            passed = True
            asteroids = list(q)
            for i in range(len(asteroids) - 1):
                if asteroids[i] > 0 and asteroids[i + 1] < 0:
                    passed = False
                    break

        return asteroids

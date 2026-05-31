class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        pref = list(accumulate(asteroids, initial=mass))
        for i in range(len(pref) - 1):
            if asteroids[i] > pref[i]:
                return False
        return True

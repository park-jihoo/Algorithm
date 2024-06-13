class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 12 12 14 19 19
        # 2  7  17 19 20
        seats.sort()
        students.sort()
        return sum(abs(x - y) for x, y in zip(seats, students))

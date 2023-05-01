class Solution:
    def average(self, salary: List[int]) -> float:
        # easy!
        salary = sorted(salary)
        return sum(salary[1:len(salary) - 1])/(len(salary) - 2)
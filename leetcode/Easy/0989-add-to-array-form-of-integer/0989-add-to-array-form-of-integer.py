class Solution:
    sys.set_int_max_str_digits(20000)

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(x) for x in str(int("".join([str(x) for x in num])) + k)]

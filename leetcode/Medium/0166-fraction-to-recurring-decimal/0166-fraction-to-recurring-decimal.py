class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        neg = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        d, m = divmod(numerator, denominator)
        ans = "-" if neg else ""
        ans += str(d) + "."

        rems = {}
        decimal = []
        while m != 0:
            if m in rems:
                idx = rems[m]
                decimal.insert(idx, "(")
                decimal.append(")")
                break
            rems[m] = len(decimal)
            m *= 10
            decimal.append(str(m // denominator))
            m %= denominator
        return ans + "".join(decimal)

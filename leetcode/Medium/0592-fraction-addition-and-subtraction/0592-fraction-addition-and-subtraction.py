class Solution:
    def fractionAddition(self, expression: str) -> str:
        elist = expression.replace("-", "+-").split("+")
        mot, son = 0, 1
        for f in elist:
            if f:
                m, s = map(int, f.split("/"))
                mot = mot * s + son * m
                son *= s
        gcd = math.gcd(mot, son)
        return str(mot // gcd) + "/" + str(son // gcd)

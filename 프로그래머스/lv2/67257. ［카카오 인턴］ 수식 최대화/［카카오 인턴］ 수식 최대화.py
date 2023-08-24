def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == "*":
        return str(
            eval("*".join([calc(priority, n + 1, e) for e in expression.split("*")]))
        )
    if priority[n] == "+":
        return str(
            eval("+".join([calc(priority, n + 1, e) for e in expression.split("+")]))
        )
    if priority[n] == "-":
        return str(
            eval("-".join([calc(priority, n + 1, e) for e in expression.split("-")]))
        )


def solution(expression):
    answer = 0
    priority = [
        ("*", "-", "+"),
        ("*", "+", "-"),
        ("+", "-", "*"),
        ("+", "*", "-"),
        ("-", "+", "*"),
        ("-", "*", "+"),
    ]
    for prior in priority:
        res = int(calc(prior, 0, expression))
        answer = max(answer, abs(res))
    return answer

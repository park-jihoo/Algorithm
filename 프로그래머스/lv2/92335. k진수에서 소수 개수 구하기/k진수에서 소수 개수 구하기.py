def is_prime_number(x):
    if x == 1:
        return False
    if x== 2:
        return True
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

def nth(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1] 

def solution(n, k):
    answer = 0
    newn = nth(n, k)
    for i in newn.split('0'):
        if i.isdigit() and is_prime_number(int(i)):
            answer+=1
    return answer
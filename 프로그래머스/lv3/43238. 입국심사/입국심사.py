def solution(n, times):
    left = 1
    right = max(times)*n
    answer = 0
    while left<=right:
        mid = (left+right)//2
        people = 0
        for i in times:
            people+=mid//i
            if people>=n:
                break
        if people>=n:
            right=mid-1
            answer = mid
        elif people<n:
            left = mid+1
    return answer
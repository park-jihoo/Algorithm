class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        time, free, ans=0, [], 0
        for i in range(len(startTime)):
            free.append(startTime[i]-time)
            ans, time = max(ans,startTime[i]-time), endTime[i]
        free.append(eventTime-time)
        left, maxi, right=0, 0, 0
        st=[0]*(len(free))
        for i in range(len(free)-1,0,-1):
            maxi=max(maxi,free[i])
            st[i]=maxi
        for i in range(len(free)-1):
            want=endTime[i]-startTime[i]
            if i>=1:
                left=max(left,free[i-1])
            if i+2<len(free):
                right=st[i+2]
            else:
                right=0
            if max(left,right)>=want:
                ans=max(ans,free[i]+free[i+1]+want)
            else:
                ans=max(ans,free[i]+free[i+1])
        return ans
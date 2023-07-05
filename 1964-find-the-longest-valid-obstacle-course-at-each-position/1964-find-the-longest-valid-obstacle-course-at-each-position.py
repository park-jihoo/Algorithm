import bisect

class Solution:
    
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # Array # Binary Search # Binary Indexed Truee
        answer = [1 for i in obstacles]
        mono = []
        for idx, obs in enumerate(obstacles):
            if not mono or mono[-1] <= obs:
                mono.append(obs)
                answer[idx] = len(mono)
            else:
                j = bisect.bisect_right(mono, obs)
                mono[j] = obs
                answer[idx] = j + 1
        return answer
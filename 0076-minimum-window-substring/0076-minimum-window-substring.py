class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        hash_t = [0]*128
        hash_s = [0]*128
        for i in range(len(t)):
            hash_t[ord(t[i])]+=1
        
        start, from_index, min_length = 0, -1, float('inf')
        
        count = 0
        for i in range(len(s)):
            hash_s[ord(s[i])]+=1
            if(hash_s[ord(s[i])] <= hash_t[ord(s[i])]):
                count+=1
            if count == len(t):
                while(hash_s[ord(s[start])] > hash_t[ord(s[start])] or hash_t[ord(s[start])]  == 0):
                    if(hash_s[ord(s[start])]> hash_t[ord(s[start])]):
                        hash_s[ord(s[start])] -=1
                    start +=1
                length = i - start + 1
                if min_length > length:
                    min_length = length
                    from_index = start
        
        if from_index == -1:
            return ""
        return s[from_index: from_index+min_length]
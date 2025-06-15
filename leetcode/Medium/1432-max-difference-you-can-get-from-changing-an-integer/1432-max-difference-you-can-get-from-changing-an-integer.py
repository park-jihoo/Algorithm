class Solution:
    def maxDiff(self, v: int) -> int:
        s = str(v)
        return (int(s.replace((s+'_').lstrip('9')[0],'9')) - 
            ((m:=search(r'[2-9]',s)) and int(s.replace(m[0],'01'[s[0]>'1'])) or v))
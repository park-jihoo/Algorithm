class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        if n == 0:
            return ""
        
        cols = n // rows
        
        result = []
        
        for c in range(cols):
            for r in range(rows):
                idx = r * cols + (c + r)  
                if c + r < cols:         
                    result.append(encodedText[idx])

        return ''.join(result).rstrip(' ')
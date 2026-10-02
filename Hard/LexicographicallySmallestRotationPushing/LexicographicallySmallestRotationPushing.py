class Solution:
    def lexiString(self, s: str) -> str:
        n = len(s)
        i, j, k = 0, 1, 0
        
        while i < n and j < n and k < n:
            if s[(i + k) % n] == s[(j + k) % n]:
                k += 1
            
            elif s[(i + k) % n] > s[(j + k) % n]:
                i += k + 1
                if i == j:
                    i += 1
                    
                k = 0
            
            else:
                j += k + 1
                if i == j:
                    j += 1
                    
                k = 0
                
        start = min(i, j)
        return s[start:] + s[:start]
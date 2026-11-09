class Solution:
    def getCount (self, s, k):
        if not s:
            return 0
            
        a = {}
        prev_char = None
        
        for c in s:
            if c != prev_char:
                a[c] = a.get(c, 0) + 1
                prev_char = c
            
        res = sum(1 for count in a.values() if count == k)
        return res
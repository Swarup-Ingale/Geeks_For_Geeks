class Solution:
    def minFlips(self, s):
        flip0 = 0
        flip1 = 0
        
        for i, c in enumerate(s):
            exp0 = '0' if i % 2 == 0 else '1'
            exp1 = '1' if i % 2 == 0 else '0'
            
            if c != exp0:
                flip0 += 1
            if c != exp1:
                flip1 += 1
                
        return min(flip0, flip1)
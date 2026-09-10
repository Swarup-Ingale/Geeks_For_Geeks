class Solution:

    def pairCount(self, x, y):
        if y % x != 0:
            return 0
            
        target = y // x
        k = 0
        d = 2
        
        while d * d <= target:
            if target % d == 0:
                k += 1
                while target % d == 0:
                    target //= d
            d += 1
                
        if target > 1:
            k += 1
            
        return 1 << k
class Solution:
    def minOperation(self, n):
        ops = 0
        while n > 0:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1
            ops += 1
        return ops
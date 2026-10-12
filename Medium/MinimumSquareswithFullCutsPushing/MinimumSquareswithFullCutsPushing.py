class Solution:
    def minSquares(self, n, m):
        count = 0

        while m > 0:
            count += n // m
            n, m = m, n % m

        return count
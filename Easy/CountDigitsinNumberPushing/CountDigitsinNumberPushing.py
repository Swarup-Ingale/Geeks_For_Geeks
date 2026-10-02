class Solution:
    def countDigits(self, n: int) -> int:
        a = str(n)
        c = 0
        for i in a:
            c += 1
        return c
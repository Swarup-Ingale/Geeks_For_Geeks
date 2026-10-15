class Solution:

    def maxValue(self, n: int) -> int:
        count = 0

        for i in range(31, -1, -1):
            if (n >> i) & 1:
                count += 1

                if count == 3:
                    n &= ~(1 << i)
                    count = 0
            else:
                count = 0

        return n
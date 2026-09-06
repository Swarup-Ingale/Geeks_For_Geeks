class Solution:
    def pairAndSum(self, arr):
        total_sum = 0

        for bit in range(32):
            count = 0
            for num in arr:
                if num & (1 << bit):
                    count += 1

            pairs = (count * (count - 1)) // 2

            total_sum += pairs * (1 << bit)

        return total_sum
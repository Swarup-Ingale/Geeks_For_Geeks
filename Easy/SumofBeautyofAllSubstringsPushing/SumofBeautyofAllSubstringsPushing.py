class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1

                max_f = -1
                min_f = float('inf')

                for count in freq:
                    if count > 0:
                        if count > max_f:
                            max_f = count
                        if count < min_f:
                            min_f = count

                total_beauty += (max_f - min_f)

        return total_beauty
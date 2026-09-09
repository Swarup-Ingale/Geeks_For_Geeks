class Solution:
    def findMax(self, n):
        def get_digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
            
        ans = n
        max_sum = get_digit_sum(n)
        
        b = 1
        while n // b > 0:
            temp = n - (n % b) - 1
            if temp > 0:
                s = get_digit_sum(temp)
                if s > max_sum or (s == max_sum and temp > ans):
                    max_sum = s
                    ans = temp
            b *= 10
            
        return ans
class Solution:

    def nthCharacter(self, n):
        len_digits = 1
        count = 9
        start = 1

        while n > len_digits * count:
            n -= len_digits * count
            len_digits += 1
            count *= 10
            start *= 10

        target_num = start + (n - 1) // len_digits

        digit_index = (n - 1) % len_digits
        
        return str(target_num)[digit_index]
class Solution:
    def sameMod(self, arr):
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(arr)

        if n <= 1:
            return -1

        diff_gcd = 0

        for i in range(1, n):
            diff_gcd = get_gcd(diff_gcd, abs(arr[i] - arr[0]))

        if diff_gcd == 0:
            return -1

        divisors = 0
        i = 1
        while i * i <= diff_gcd:
            if diff_gcd % i == 0:
                divisors += 1
                if i * i != diff_gcd:
                    divisors += 1
            i += 1

        return divisors
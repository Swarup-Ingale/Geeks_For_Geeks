class Solution:
    def findXOR(self, l: int, r: int) -> int:
        def xor_till(n: int) -> int:
            rem = n % 4
            if rem == 0:
                return n
            elif rem == 1:
                return 1
            elif rem == 2:
                return n + 1
            else:
                return 0

        return xor_till(r) ^ xor_till(l - 1)
class Solution:
	def makeZero(self, arr: list[int]) -> bool:
        xor = 0
        for v in arr:
            xor ^= v
            
        if xor == 0:
            return 0
            
        return 0 if len(arr) % 2 == 0 else 1
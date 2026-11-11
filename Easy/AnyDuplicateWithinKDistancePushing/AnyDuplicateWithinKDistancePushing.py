class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        a = {}
        for i, n in enumerate(arr):
            if n in a and i - a[n] <= k:
                return True
        
            a[n] = i
        return False
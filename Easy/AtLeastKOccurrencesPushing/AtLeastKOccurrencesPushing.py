class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        elements = {}
        for n in arr:
            elements[n] = elements.get(n, 0) + 1
            if elements[n] == k:
                return n
            
        return -1
class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr)
        half = n // 2
        
        left = sorted(arr[:half])
        right = sorted(arr[half:])
        
        count = 0
        j = 0
        
        for i in range(half):
            while j < half and left[i] >= 5 * right[j]:
                j += 1
                
            count += j
            
        return count
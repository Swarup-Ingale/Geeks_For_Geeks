class Solution:

    def maximumSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        
        max_no_square = arr[0]
        max_squared = arr[0] * arr[0]
        ans = max(max_no_square, max_squared)
        
        for i in range(1, n):
            val = arr[i]
            val_sq = val * val
            
            new_max_sq = max(val_sq, val_sq + max_no_square, val + max_squared)
            new_max_no_sq = max(val, val + max_no_square)
            
            max_squared = new_max_sq
            max_no_square = new_max_no_sq
            
            ans = max(ans, max_no_square, max_squared)
            
        return ans
class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        n = len(arr)
        
        if m >= n:
            return sum(arr)
            
        current_sum = sum(arr[:m])
        max_sum = current_sum
        
        for i in range(1, n):
            current_sum = current_sum - arr[i - 1] + arr[(i + m - 1) % n]
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum
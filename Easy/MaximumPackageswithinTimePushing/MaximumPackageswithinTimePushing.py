class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        n = len(arr)
        if totalTime >= n:
            return sum(arr)
            
        curr_sum = sum(arr[:totalTime])
        max_sum = curr_sum
        
        for i in range(totalTime, n):
            curr_sum += arr[i] - arr[i - totalTime]
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum
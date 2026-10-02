class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)
        pref = [0] * (n + 1)
        
        for i in range(n):
            pref[i + 1] = pref[i] + arr[i]
        
        max_sum = float('-inf')
        min_pref = 0
        
        for i in range(k, n + 1):
            min_pref = min(min_pref, pref[i - k])
            current_sum = pref[i] - min_pref
            max_sum = max(max_sum, current_sum)
            
        return max_sum
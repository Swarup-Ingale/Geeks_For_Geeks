class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        if n < k:
            return 0
            
        window_xor = 0
        for i in range(k):
            window_xor ^= arr[i]
            
        max_xor = window_xor
        
        for i in range(k, n):
            window_xor ^= arr[i] ^ arr[i - k]
            max_xor = max(max_xor, window_xor)
            
        return max_xor
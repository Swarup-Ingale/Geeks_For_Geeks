class Solution:
    def findMaxProduct(self, arr, k):
        n = len(arr)
        window_prod = 1
        for i in range(k):
            window_prod *= arr[i]
        max_prod = window_prod
        
        for i in range(k, n):
            window_prod = (window_prod * arr[i]) // arr[i - k]
            max_prod = max(max_prod, window_prod)
            
        return max_prod
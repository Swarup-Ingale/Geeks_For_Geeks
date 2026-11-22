class Solution:
	def longestSubarrayDivK(self, arr, k):
	    first_idx = {0: -1}
        prefix_sum = 0
        max_len = 0
        
        for i, val in enumerate(arr):
            prefix_sum += val
            rem = prefix_sum % k
        
            if rem in first_idx:
                max_len = max(max_len, i - first_idx[rem])
            else:
                first_idx[rem] = i
        
        return max_len
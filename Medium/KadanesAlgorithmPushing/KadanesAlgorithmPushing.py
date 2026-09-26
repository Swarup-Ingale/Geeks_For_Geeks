class Solution:
    def maxSubarraySum(self, arr):
        curr_max, max_now = 0, float('-inf')
        for c in arr:
            curr_max = max(c, curr_max + c)
            max_now = max(max_now, curr_max)
        return max_now
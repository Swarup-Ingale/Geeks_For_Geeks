class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)

        left_max = [0] * n
        left_min = [0] * n
        right_max = [0] * n
        right_min = [0] * n

        curr_max = 0
        max_so_far = float('-inf')
        curr_min = 0
        min_so_far = float('inf')
        
        for i in range(n):
            curr_max = max(arr[i], curr_max + arr[i])
            max_so_far = max(max_so_far, curr_max)
            left_max[i] = max_so_far

            curr_min = min(arr[i], curr_min + arr[i])
            min_so_far = min(min_so_far, curr_min)
            left_min[i] = min_so_far
        
        curr_max = 0
        max_so_far = float('-inf')
        curr_min = 0
        min_so_far = float('inf')
        
        for i in range(n - 1, -1, -1):
            curr_max = max(arr[i], curr_max + arr[i])
            max_so_far = max(max_so_far, curr_max)
            right_max[i] = max_so_far

            curr_min = min(arr[i], curr_min + arr[i])
            min_so_far = min(min_so_far, curr_min)
            right_min[i] = min_so_far

        max_diff = float('-inf')
        
        for i in range(n - 1):
            diff1 = abs(left_max[i] - right_min[i + 1])
            diff2 = abs(left_min[i] - right_max[i + 1])
        
            max_diff = max(max_diff, diff1, diff2)
        
        return max_diff
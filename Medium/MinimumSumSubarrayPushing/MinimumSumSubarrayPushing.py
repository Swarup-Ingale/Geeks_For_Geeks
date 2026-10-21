class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        current_min = arr[0]
        global_min = arr[0]

        for i in range(1, len(arr)):

            current_min = min(arr[i], current_min + arr[i])

            global_min = min(global_min, current_min)
            
        return global_min
class Solution:
    def maxFrequency(self, arr, k):
        arr.sort()
        left = 0
        current_sum = 0
        max_freq = 0
        
        for right in range(len(arr)):
            current_sum += arr[right]
            while arr[right] * (right - left + 1) - current_sum > k:
                current_sum -= arr[left]
                left += 1
            if right - left + 1 > max_freq:
                max_freq = right - left + 1
        return max_freq
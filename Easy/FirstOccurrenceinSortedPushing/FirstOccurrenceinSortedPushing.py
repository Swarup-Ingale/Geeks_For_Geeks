class Solution:
    def firstSearch(self, arr, k):
        left = 0
        right = len(arr) - 1
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == k:
                ans = mid
                right = mid - 1
            elif arr[mid] > k:
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
        
        return ans
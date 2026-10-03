class Solution:
    def binarySearch(self, arr, k):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == k:
                return True
            elif arr[mid] > k:
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
                
        return False
class Solution:
    def find(self, arr, x):
        left = 0
        right = len(arr) - 1
        first = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == x:
                first = mid
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
            
        if first == -1:
            return [-1, -1]
            
        left = first
        right = len(arr) - 1
        last = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == x:
                last = mid
                left = mid + 1
            elif arr[mid] < x:
                left = left + 1
            else:
                right = mid - 1
        return [first, last]
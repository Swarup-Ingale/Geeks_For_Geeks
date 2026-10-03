class Solution:
    def search(self, arr, key):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == key:
                return mid
                
            if arr[left] <= arr[mid]:
                if arr[left] <= key < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if arr[mid] < key <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
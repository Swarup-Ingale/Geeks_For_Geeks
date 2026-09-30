class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)
        
        for i in range(n - 2):
            if arr[i] + arr[i + 1] + arr[i + 2] > target:
                break
            
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return False
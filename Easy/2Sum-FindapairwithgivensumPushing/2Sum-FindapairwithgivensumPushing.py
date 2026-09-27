class Solution:
    def twoSum(self, arr, target):
        n = len(arr)
        arr.sort()
        l = 0
        r = n - 1
        
        while n != 0 and l < r:
            if arr[l] + arr[r] == target:
                return [arr[l], arr[r]]
            else:
                if arr[l] + arr[r] > target:
                    r -= 1
                else:
                    l += 1
        return []
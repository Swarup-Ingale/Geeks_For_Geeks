class Solution:
    def maxWater(self, arr):
        n = len(arr)
        i = 0
        j = n - 1
        b = []
        
        while n != 0 or i < j:
            if arr[i] <= arr[j]:
                b.append((j - i) * arr[i])
                i += 1
            elif arr[j] < arr[i]:
                b.append((j - i) * arr[j])
                j -= 1
            n -= 1
        
        return max(b)
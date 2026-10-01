class Solution:
    def getPairs(self, arr):
        arr.sort()
        res = []
        l = 0
        r = len(arr) - 1
        
        while l < r:
            c_s = arr[r] + arr[l]
            
            if c_s == 0:
                res.append([arr[l], arr[r]])
                
                while l < r and arr[l] == arr[l + 1]:
                    l += 1
                
                while l < r and arr[r] == arr[r - 1]:
                    r -= 1
                    
                l += 1
                r -= 1
            
            elif c_s < 0:
                l += 1
            else:
                r -= 1
            
        return res
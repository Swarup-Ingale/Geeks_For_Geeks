class Solution:
    def modifyArray(self, arr): 
        i = 0
        n = len(arr)
        if n <= 1:
            return arr
            
        for i in range(n - 1):
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] = 2 * arr[i]
                arr[i + 1] = 0
                
        count = 0
        
        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
            
        while count < n:
            arr[count] = 0
            count += 1
            
        return arr
                
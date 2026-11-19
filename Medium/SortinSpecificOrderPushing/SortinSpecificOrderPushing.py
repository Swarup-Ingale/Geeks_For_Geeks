class Solution:
    def sortIt(self, arr):
        even = []
        odd = []
        
        for n in arr:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
                
        even.sort()
        odd.sort(reverse=True)
        
        arr[:] = odd + even
        return arr
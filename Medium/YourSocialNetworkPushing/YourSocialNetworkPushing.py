class Solution:
    def socialNetwork(self, arr):
        n = len(arr) + 1
        res = []
        
        for i in range(2, n + 1):
            reach = {}
            curr = i
            k = 0
            
            while curr > 1:
                friend = arr[curr - 2]
                k += 1
                reach[friend] = k
                curr = friend
            
            for j in range(1, i):
                if j in reach:
                    res.append([i, j, reach[j]])
            
        return res
class Solution:
    def countPairs(self, arr, target):
        freq = {}
        count = 0
        
        for n in arr:
            needed = target - n
            
            if needed in freq:
                count += freq[needed]
            
            freq[n] = freq.get(n, 0) + 1
            
        return count
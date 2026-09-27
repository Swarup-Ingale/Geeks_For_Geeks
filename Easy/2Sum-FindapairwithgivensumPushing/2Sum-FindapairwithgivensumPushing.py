class Solution:
    def twoSum(self, arr, target):
        seen = set()
        
        for n in arr:
            com = target - n
            if com in seen:
                return [com, n]
            seen.add(n)
        
        return []
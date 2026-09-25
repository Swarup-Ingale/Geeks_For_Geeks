class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        counter = {}
        for char in s1:
            counter[char] = counter.get(char, 0) + 1
        
        for char in s2:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
            
        return True
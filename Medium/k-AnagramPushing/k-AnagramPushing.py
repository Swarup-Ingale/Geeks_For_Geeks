class Solution:
    def areKAnagrams(self, s1, s2, k):
        if len(s1) != len(s2):
            return False
        
        count1 = {}
        need_changes = 0
        
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        
        for char in s2:
            if count1.get(char, 0) > 0:
                count1[char] -= 1
            else:
                need_changes += 1
            
        return need_changes <= k
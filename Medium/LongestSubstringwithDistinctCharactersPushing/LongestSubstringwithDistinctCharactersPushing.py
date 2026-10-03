class Solution:
    def longestUniqueSubstr(self, s):
        char = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            
            char.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len
class Solution:
    def longestKSubstr(self, s, k):
        char = {}
        left = 0
        max_len = -1
        
        for right in range(len(s)):
            char[s[right]] = char.get(s[right], 0) + 1
            
            while len(char) > k:
                char[s[left]] -= 1
                if char[s[left]] == 0:
                    del char[s[left]]
                left += 1
                
            if len(char) == k:
                max_len = max(max_len, right - left + 1)
                
        return max_len
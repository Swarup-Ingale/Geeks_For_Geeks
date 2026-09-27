class Solution:
    def isPalindrome(self, s):
        n = len(s)
        if not s:
            return True
            
        i = 0
        while n != 0:
            if i < n - 1:
                if s[i] != s[n - 1]:
                    return False
            i += 1
            n -= 1
            
        return True
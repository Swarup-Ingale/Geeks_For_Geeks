class Solution:
    def canFormPalindrome(self, s):
        count = 0
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in counter:
            if counter[char] % 2 != 0:
                count += 1
                if count > 1:
                    return False
        
        return True
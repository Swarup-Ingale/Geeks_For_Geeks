class Solution:
	def isPalinSent(self, s):
		s = "".join(i for i in s if i.isalnum())
		s = s.lower()
		n = len(s)
		
		i = 0
        while n != 0:
            if i < n - 1:
                if s[i] != s[n - 1]:
                    return False
            i += 1
            n -= 1
            
        return True
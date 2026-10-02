class Solution:
    def search(self, txt, pat):
        if len(pat) > len(txt):
            return False
        
        c1 = {}
        c2 = {}
        
        for i in range(len(pat)):
            c1[pat[i]] = c1.get(pat[i], 0) + 1
            c2[txt[i]] = c2.get(txt[i], 0) + 1
            
        if c1 == c2:
            return True
        
        left = 0
        for right in range(len(pat), len(txt)):
            c2[txt[right]] = c2.get(txt[right], 0) + 1
            c2[txt[left]] -= 1
            
            if c2[txt[left]] == 0:
                del c2[txt[left]]
                
            left += 1
            
            if c1 == c2:
                return True
                
        return False
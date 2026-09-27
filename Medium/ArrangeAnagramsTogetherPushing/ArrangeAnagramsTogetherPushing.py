from collections import defaultdict

class Solution:
    def anagrams(self, arr):
        ans = defaultdict(list)
        
        for a in arr:
            n = [0] * 26
            for i in a:
                n[ord(i) - ord("a")] += 1
            ans[tuple(n)].append(a)
            
        return list(ans.values())
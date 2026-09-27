class Solution:

    def minOperations(self, arr):
        st = set()
        
        for x in arr:
            if x > 0:
                st.add(x)
                
        return len(st)
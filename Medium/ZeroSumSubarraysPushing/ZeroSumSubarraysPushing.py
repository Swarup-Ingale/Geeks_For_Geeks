class Solution:
    def findSubarray(self, arr):
        if not arr:
            return 1
        k = 0
        sub_num = {0:1}
        t = c = 0

        for n in arr:
            t += n
            if t - k in sub_num:
                c += sub_num[t - k]
            sub_num[t] = 1 + sub_num.get(t, 0)

        return c
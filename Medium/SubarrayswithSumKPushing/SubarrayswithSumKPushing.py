class Solution:
    def cntSubarrays(self, arr, k):
        sub_nums = {0:1}
        t = c = 0
        for n in arr:
            t += n
            if t - k in sub_nums:
                c += sub_nums[t - k]
            sub_nums[t] = 1 + sub_nums.get(t, 0)
        return c
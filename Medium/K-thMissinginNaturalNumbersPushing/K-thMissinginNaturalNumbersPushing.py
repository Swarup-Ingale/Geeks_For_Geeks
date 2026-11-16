class Solution:
    def findKthSmall(self, arr, k):
        arr.sort()

        ans = k
        for num in arr:
            if num <= ans:
                ans += 1
            else:
                break

        return ans
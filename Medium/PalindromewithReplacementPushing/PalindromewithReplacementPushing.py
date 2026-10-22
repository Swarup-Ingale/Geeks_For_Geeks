class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        ans = 0
        prev_char = None

        for i in range((n + 1) // 2):
            left = s[i]
            right = s[n - 1 - i]

            if left != '?' and right != '?' and left != right:
                return -1

            c = '?'
            if left != '?':
                c = left
            elif right != '?':
                c = right

            if c != '?':
                if prev_char is not None:
                    ans += abs(ord(c) - ord(prev_char))
                prev_char = c

        return ans * 2

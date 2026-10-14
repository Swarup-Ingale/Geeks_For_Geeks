class Solution:
    def findRollOut(self, s, roll):
        n = len(s)
        diff = [0] * (n + 1)

        for r in roll:
            diff[0] += 1
            diff[r] -= 1

        res = []
        curr_rolls = 0

        for i in range(n):
            curr_rolls += diff[i]

            shift = curr_rolls % 26

            new_char = chr((ord(s[i]) - 97 + shift) % 26 + 97)
            res.append(new_char)

        return "".join(res)
class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        n = len(s1)
        p1, p2 = 0, 0

        while p1 < n or p2 < n:
            while p1 < n and s1[p1] == '#':
                p1 += 1
            while p2 < n and s2[p2] == '#':
                p2 += 1

            if p1 == n and p2 == n:
                return True

            if p1 == n or p2 == n:
                return False

            if s1[p1] != s2[p2]:
                return False

            if s1[p1] == 'A' and p1 < p2:
                return False

            if s1[p1] == 'B' and p1 > p2:
                return False

            p1 += 1
            p2 += 1

        return True
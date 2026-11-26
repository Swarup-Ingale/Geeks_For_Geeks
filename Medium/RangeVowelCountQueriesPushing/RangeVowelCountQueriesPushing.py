class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        vowels = set("aeiou")
        pref = [0] * (len(s) + 1)

        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (1 if ch in vowels else 0)

        return [pref[r + 1] - pref[l] for l, r in queries]
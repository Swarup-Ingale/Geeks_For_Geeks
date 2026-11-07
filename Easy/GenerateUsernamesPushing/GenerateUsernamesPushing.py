class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)
        assigned = set()

        next_suffix = {}
        ans = []

        for s in arr:
            if s not in assigned:
                assigned.add(s)
                ans.append(s)
            else:
                k = next_suffix.get(s, 1)

                while f"{s}{k}" in reserved or f"{s}{k}" in assigned:
                    k += 1

                next_suffix[s] = k + 1

                new_name = f"{s}{k}"
                assigned.add(new_name)
                ans.append(new_name)

        return ans
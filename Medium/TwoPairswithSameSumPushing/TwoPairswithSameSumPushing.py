class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        seen_pairs: dict[int, tuple[int, int]] = {}
        best: list[int] | None = None

        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s in seen_pairs:
                    p, q = seen_pairs[s]
                    if p != i and p != j and q != i and q != j:
                        quad = [p, q, i, j]
                        if best is None or quad < best:
                            best = quad
                else:
                    seen_pairs[s] = (i, j)

        return best if best is not None else [-1, -1, -1, -1]
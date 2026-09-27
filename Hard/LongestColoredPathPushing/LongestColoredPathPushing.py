class Solution:
    def longestPath(self, s, edges):
        n = len(s)
        if n <= 1:
            return n

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        order = []
        parent = [-1] * n
        stack = [0]

        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)

        order.reverse()

        R = [0] * n
        B = [0] * n
        RB = [0] * n
        BR = [0] * n
        ans = 1

        for u in order:
            max_R = max_B = max_RB = max_BR = 0

            for v in adj[u]:
                if v == parent[u]:
                    continue

                if s[u] == 'R':
                    if max_R + RB[v] + 1 > ans: ans = max_R + RB[v] + 1
                    if max_RB + R[v] + 1 > ans: ans = max_RB + R[v] + 1
                else:
                    if max_BR + B[v] + 1 > ans: ans = max_BR + B[v] + 1
                    if max_B + BR[v] + 1 > ans: ans = max_B + BR[v] + 1

                if R[v] > max_R: max_R = R[v]
                if B[v] > max_B: max_B = B[v]
                if RB[v] > max_RB: max_RB = RB[v]
                if BR[v] > max_BR: max_BR = BR[v]

            if s[u] == 'R':
                R[u] = 1 + max_R
                B[u] = 0
                RB[u] = 1 + max_RB
                BR[u] = R[u]
            else:
                R[u] = 0
                B[u] = 1 + max_B
                RB[u] = B[u]
                BR[u] = 1 + max_BR

            if R[u] > ans: ans = R[u]
            if B[u] > ans: ans = B[u]
            if RB[u] > ans: ans = RB[u]
            if BR[u] > ans: ans = BR[u]

        return ans
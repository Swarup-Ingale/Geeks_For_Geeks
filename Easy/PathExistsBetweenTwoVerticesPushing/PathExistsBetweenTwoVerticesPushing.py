from collections import deque

class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        if u == v:
            return True

        n = len(adj)
        visited = [False] * n
        visited[u] = True
        q = deque([u])

        while q:
            curr = q.popleft()
            if curr == v:
                return True
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

        return False
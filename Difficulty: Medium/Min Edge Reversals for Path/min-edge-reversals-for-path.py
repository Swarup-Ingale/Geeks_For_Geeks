class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        if src == dst:
            return 0

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append((v, 0))
            adj[v].append((u, 1))
        dist = [float('inf')] * (n + 1)
        dist[src] = 0

        curr_q = [src]
        next_q = []

        while curr_q or next_q:
            if not curr_q:
                curr_q = next_q
                next_q = []

            u = curr_q.pop()

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

                    if w == 0:
                        curr_q.append(v)
                    else:
                        next_q.append(v)

        return dist[dst] if dist[dst] != float('inf') else -1
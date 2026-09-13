class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        n = len(adj)

        if n <= 1:
            return 0

        is_1_based = False
        for row in adj:
            for val in row:
                if val == n:
                    is_1_based = True
                    break
            if is_1_based:
                break

        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            queue = [start]
            farthest_node = start
            max_dist = 0

            head = 0
            while head < len(queue):
                node = queue[head]
                head += 1

                for neighbor in adj[node]:
                    v = neighbor - 1 if is_1_based else neighbor

                    if dist[v] == -1:
                        dist[v] = dist[node] + 1
                        queue.append(v)
                        if dist[v] > max_dist:
                            max_dist = dist[v]
                            farthest_node = v

            return farthest_node, max_dist

        farthest_A, _ = bfs(0)

        _, diameter = bfs(farthest_A)

        return (diameter + 1) // 2
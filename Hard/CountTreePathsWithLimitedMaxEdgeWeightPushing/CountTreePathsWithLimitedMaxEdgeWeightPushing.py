class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.total_paths = 0

    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # The number of new valid paths is size of component A * size of component B
            self.total_paths += self.size[root_i] * self.size[root_j]

            # Merge the smaller component into the larger one to keep the tree shallow
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i

            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

class Solution:
    def maximumWeight(self, n: int, edges: list[list[int]], queries: list[int]) -> list[int]:
        # Sort edges based on weight in ascending order
        edges.sort(key=lambda x: x[2])

        # Pair queries with their original indices and sort them
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        ans = [0] * len(queries)
        dsu = DSU(n)

        edge_idx = 0
        num_edges = len(edges)

        for q_val, original_idx in sorted_queries:
            # Add all edges that have a weight <= current query
            while edge_idx < num_edges and edges[edge_idx][2] <= q_val:
                u, v, w = edges[edge_idx]
                dsu.union(u, v)
                edge_idx += 1

            # Record the accumulated paths in their original query order
            ans[original_idx] = dsu.total_paths

        return ans
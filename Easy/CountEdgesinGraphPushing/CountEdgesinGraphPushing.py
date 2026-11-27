class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        total_degree = sum(len(neighbors) for neighbors in adj)
        return total_degree // 2
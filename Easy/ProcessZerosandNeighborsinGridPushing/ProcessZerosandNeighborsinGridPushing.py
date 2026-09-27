class Solution:
    def makeZeros(self, mat):
        m = len(mat)
        n = len(mat[0])

        zero_positions = []
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    zero_positions.append((r, c))

        if not zero_positions:
            return

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        updates = []

        for r, c in zero_positions:
            current_sum = 0
            neighbors_to_zero = []

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    current_sum += mat[nr][nc]
                    neighbors_to_zero.append((nr, nc))

            updates.append((r, c, current_sum, neighbors_to_zero))

        for r, c, total_sum, neighbors in updates:
            mat[r][c] = total_sum
            for nr, nc in neighbors:
                mat[nr][nc] = 0

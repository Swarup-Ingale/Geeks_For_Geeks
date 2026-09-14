from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        if not mat or not mat[0]:
            return -1
            
        n, m = len(mat), len(mat[0])
        safe = [[True] * m for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = False
                    
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m:
                            safe[ni][nj] = False
                            
        queue = deque()
        
        for i in range(n):
            if safe[i][0]:
                queue.append((i, 0, 1))
                safe[i][0] = False
                
        while queue:
            r, c, dist = queue.popleft()
            if c == m - 1:
                return dist
                
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                
                if 0 <= nr < n and 0 <= nc < m and safe[nr][nc]:
                    safe[nr][nc] = False
                    queue.append((nr, nc, dist + 1))
                    
        return -1
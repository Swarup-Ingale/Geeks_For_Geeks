class Solution:
	def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
        start_x, start_y = knightPos[0] - 1, knightPos[1] - 1
        target_x, target_y = targetPos[0] - 1, targetPos[1] - 1
		
        if start_x == target_x and start_y == target_y:
            return 0
        
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        visited = [[False] * n for _ in range(n)]
        visited[start_x][start_y] = True
        
        queue = [(start_x, start_y, 0)]
        head = 0
        
        while head < len(queue):
            curr_x, curr_y, steps = queue[head]
            head += 1
            
            for dx, dy in moves:
                next_x = curr_x + dx
                next_y = curr_y + dy
                
                if next_x == target_x and next_y == target_y:
                    return steps + 1
                    
                if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, steps + 1))
                    
        return -1
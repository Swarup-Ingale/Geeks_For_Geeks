class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        curr_x, curr_y = 0, 0
        min_x, max_x = 0, 0
        min_y, max_y = 0, 0
        
        for move in s:
            if move == 'L':
                curr_x -= 1
            elif move == 'R':
                curr_x += 1
            elif move == 'D':
                curr_y -= 1
            elif move == 'U':
                curr_y += 1

            min_x = min(min_x, curr_x)
            max_x = max(max_x, curr_x)
            min_y = min(min_y, curr_y)
            max_y = max(max_y, curr_y)

        path_width = max_x - min_x + 1
        path_height = max_y - min_y + 1

        return path_width <= m and path_height <= n
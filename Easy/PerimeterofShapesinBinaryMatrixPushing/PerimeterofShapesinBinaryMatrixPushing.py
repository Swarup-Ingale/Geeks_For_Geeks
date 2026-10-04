from typing import List

class Solution:
    def findPerimeter(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    perimeter += 4
                
                    if r > 0 and mat[r - 1][c] == 1:
                        perimeter -= 2
                    
                    if c > 0 and mat[r][c - 1] == 1:
                        perimeter -= 2
        
        return perimeter
class Solution:
    def setMatrixZeroes(self, mat):
        m = len(mat)
        n = len(mat[0])
        col0 = 1
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    mat[r][0] = 0
                    
                    if c != 0:
                        mat[0][c] = 0
                    else:
                        col0 = 0
                
        for r in range(1, m):
            for c in range(1, n):
                if mat[r][0] == 0 or mat[0][c] == 0:
                    mat[r][c] = 0
                    
        if mat[0][0] == 0:
            for c in range(n):
                mat[0][c] = 0
            
        if col0 == 0:
            for r in range(m):
                mat[r][0] = 0
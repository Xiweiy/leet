class Solution(object):
    
    def checkOneDiagonal(self, matrix, startX, startY):
        m, n = len(matrix), len(matrix[0])
        x, y = startX, startY
        diagonal = matrix[x][y]
        while x<m and y<n:
            if matrix[x][y] != diagonal:
                return False
            x += 1
            y += 1
        return True
            
    def isToeplitzMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if not self.checkOneDiagonal(matrix, i, 0):
                return False
        for j in range(n):
            if not self.checkOneDiagonal(matrix, 0, j):
                return False
        return True

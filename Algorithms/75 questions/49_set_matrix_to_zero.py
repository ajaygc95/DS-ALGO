class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        
        visited = [[-1]*columns for _ in range(rows)]
        
        def bfs(row, col):
            for i in range(rows):
                if matrix[i][col] != 0:
                    visited[i][col] = 1
                matrix[i][col] = 0
            for j in range(columns):
                if matrix[row][j] != 0:
                    visited[row][j] =1
                matrix[row][j] = 0

        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 0 and visited[row][col] == -1:
                    bfs(row,col)
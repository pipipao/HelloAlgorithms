class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mat = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    mat[i][j] = grid[i][j]
                elif i == 0:
                    mat[i][j] = mat[i][j - 1] + grid[i][j]
                elif j == 0:
                    mat[i][j] = mat[i - 1][j] + grid[i][j]
                else:
                    mat[i][j] = min(mat[i][j - 1], mat[i - 1][j]) + grid[i][j]
        return mat[m - 1][n - 1]

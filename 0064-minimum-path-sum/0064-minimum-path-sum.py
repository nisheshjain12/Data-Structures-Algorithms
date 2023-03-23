class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        def help(i,j):
            if i==m-1 and j==n-1:
                return grid[m-1][n-1]
            if i>=m or j>=n:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            
            left=grid[i][j] + help(i,j+1)
            down=grid[i][j] + help(i+1,j)
            dp[i][j] = min(left,down)
            return dp[i][j]
        
        return help(0,0)
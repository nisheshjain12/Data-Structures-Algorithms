class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        
        def help(i,j):
            if j<0 or j>=n:
                return 10**8
            if i==n-1:
                return matrix[n-1][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            left=matrix[i][j]+help(i+1,j-1)
            down=matrix[i][j]+help(i+1,j)
            right=matrix[i][j]+help(i+1,j+1)
            
            dp[i][j] = min(left,down,right)
            return dp[i][j]
        
        mini = 10**8
        for j in range(n):
            mini = min(mini,help(0,j))
        return mini            
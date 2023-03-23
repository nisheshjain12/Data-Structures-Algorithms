class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        n=len(triangle[m-1])
        
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        
        def help(i,j):
            if i==m-1:
                return triangle[n-1][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            down=triangle[i][j] + help(i+1,j)
            right=triangle[i][j] + help(i+1,j+1)
            dp[i][j] = min(down,right)
            return dp[i][j]
        
        return help(0,0)
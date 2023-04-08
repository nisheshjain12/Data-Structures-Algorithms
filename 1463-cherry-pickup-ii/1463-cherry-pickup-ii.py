class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        
        def rec(i,j1,j2):
            if j1<0 or j2<0 or j1>=n or j2>=n:
                return -10**8
            if i==m-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            maxi=-10**8
            
            for dj1 in range(-1,2,1):
                for dj2 in range(-1,2,1):
                    val=grid[i][j1]
                    if j1 != j2:
                        val+=grid[i][j2]
                        
                    val+=rec(i+1,j1+dj1,j2+dj2)
                    maxi = max(maxi,val)
            dp[i][j1][j2] = maxi
            
            return dp[i][j1][j2]           
                    
        return rec(0,0,n-1)
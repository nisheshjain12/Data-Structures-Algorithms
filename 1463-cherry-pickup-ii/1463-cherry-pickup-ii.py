class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        

        # Base case
        for j1 in range(n):
            for j2 in range(n):
                if j1==j2:
                    dp[m-1][j1][j2] = grid[m-1][j1]
                else:
                    dp[m-1][j1][j2] = grid[m-1][j1] + grid[m-1][j2]
        
        
        for i in range(m-2,-1,-1):
            for j1 in range(n):
                for j2 in range(n):
                    
                    # DP copy 
                    maxi=-10**8
                    for dj1 in range(-1,2,1):
                        for dj2 in range(-1,2,1):
                            val=grid[i][j1]
                            if j1 != j2:
                                val+=grid[i][j2]
                            if j1+dj1>=0 and j1+dj1<n and j2+dj2>=0 and j2+dj2<n:
                                val+=dp[i+1][j1+dj1][j2+dj2]
                            else:
                                val=-10**8
                            
                            maxi = max(maxi,val)
                            
                    dp[i][j1][j2] = maxi
                    
        return dp[0][0][n-1]
       
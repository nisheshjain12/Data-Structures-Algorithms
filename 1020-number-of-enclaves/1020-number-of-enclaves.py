class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        def isValid(i,j):
            if i<0 or i>=m:
                return False
            if j<0 or j>=n:
                return False
            if grid[i][j]==0:
                return False
            return True

        def dfs(i,j):
            grid[i][j] = 0
            if isValid(i+1,j) and grid[i+1][j] == 1:
                dfs(i+1,j)
            if isValid(i-1,j) and grid[i-1][j] == 1:
                dfs(i-1,j)
            if isValid(i,j+1) and grid[i][j+1] == 1:
                dfs(i,j+1)
            if isValid(i,j-1) and grid[i][j-1] == 1:
                dfs(i,j-1)
            
        for i in range(m):
            for j in range(n):
                if i*j ==0 or i==m-1 or j==n-1:
                    if grid[i][j] == 1:
                        dfs(i,j)

        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans+=1
        
        return ans
   
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        vis = [[False for _ in range(n)]for _ in range(m)]
        arr=[]

        def valid(i,j):
            if i<0 or i>=m:
                return False
            if j<0 or j>=n:
                return False
            if grid[i][j] == 0:
                return False
            if vis[i][j] == True:
                return False
            return True

        def dfs(i,j):
            nonlocal area
            vis[i][j] = True
            area+=1
            if valid(i+1,j):
                dfs(i+1,j)
            if valid(i-1,j):
                dfs(i-1,j)
            if valid(i,j+1):
                dfs(i,j+1)
            if valid(i,j-1):
                dfs(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 1:
                    area=0
                    dfs(i,j)
                    arr.append(area)
        
        if len(arr) == 0:
            return 0
        return max(arr)

            
        



            
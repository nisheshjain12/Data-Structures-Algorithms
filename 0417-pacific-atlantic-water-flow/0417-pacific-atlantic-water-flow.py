class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pac=set()
        atl=set()

        def dfs(i,j,vis,prev):
            if (i,j) in vis or i<0 or j<0 or i>=m or j>=n or heights[i][j]<prev:
                return 
            vis.add((i,j))
            dfs(i+1,j,vis,heights[i][j])
            dfs(i-1,j,vis,heights[i][j])
            dfs(i,j+1,vis,heights[i][j])
            dfs(i,j-1,vis,heights[i][j])

        for row in range(m):
            dfs(row,0,pac,heights[row][0])
            dfs(row,n-1,atl,heights[row][n-1])
        
        for col in range(n):
            dfs(0,col,pac,heights[0][col])
            dfs(m-1,col,atl,heights[m-1][col])

        ans=[]
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    ans.append([i,j])
        return ans




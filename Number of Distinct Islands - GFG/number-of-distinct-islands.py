#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        def valid(i,j):
            if i>=0 and i<m and j>=0 and j<n and vis[i][j] == 0 and grid[i][j] == 1:
                return True
            return False
            
        row=[-1,0,1,0]
        col=[0,1,0,-1]
        vis=[[0 for _ in range(n)] for _ in range(m)]
        ans=set()
        
        def dfs(i,j,br,bc,v):
            vis[i][j] = 1
            v.append((i-br,j-bc))
            
            for x in range(4):
                nr=i+row[x]
                nc=j+col[x]

                if valid(nr,nc):
                    dfs(nr,nc,br,bc,v)
            
        
        for i in range(m):
            for j in range(n):
                if vis[i][j]==0 and grid[i][j] ==1:
                    v=[]
                    dfs(i,j,i,j,v)
                    # print(tuple(v))
                    ans.add(tuple(v))
        return len(ans)
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends
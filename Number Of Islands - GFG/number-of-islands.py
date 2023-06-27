from typing import List

class DisjointSet():
    def __init__(self,n):
        self.parent = [i for i in  range(n)]
        self.rank = [0] * n
    def findParent(self,node):
        if self.parent[node] != node:
          self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    def unionRank(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
          return 
        if self.rank[pu]<self.rank[pv]:
          self.parent[pu] = pv
        elif self.rank[pv]<self.rank[pu]:
          self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

class Solution:
    def numOfIslands(self, n: int, m : int, operators : List[List[int]]) -> List[int]:
        ds = DisjointSet((n+1)*(m+1))
        vis = [[0 for j in range(m)]for i in range(n)]
        cnt = 0
        ans = []
        for row,col in operators:
            if vis[row][col] == 1:
                ans.append(cnt)
                continue
            
            vis[row][col] = 1
            cnt +=1
            delRow = [-1,0,1,0]
            delCol = [0,1,0,-1]
            for i in range(4):
                nr = row + delRow[i]
                nc = col + delCol[i]
                if nr>=0 and nr<n and nc>=0 and nc<m:
                    if vis[nr][nc]==1:
                        nodeNo = row * m + col
                        adjNodeNo = nr*m+nc
                        if ds.findParent(nodeNo)!=ds.findParent(adjNodeNo):
                            cnt -= 1
                            ds.unionRank(nodeNo,adjNodeNo)
            ans.append(cnt)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends
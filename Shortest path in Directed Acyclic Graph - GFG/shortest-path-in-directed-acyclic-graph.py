#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
            
        adj=[[] for _ in range(n)]
        for i,j,w in edges:
            adj[i].append([j,w])
        vis=[False for _ in range(n)]
        stack=[]
        
        def toposort(node):
            vis[node] = True
            for child in adj[node]:
                if not vis[child[0]]:
                    toposort(child[0])
            stack.append(node)
        
        for i in range(n):
            if not vis[i]:
                toposort(i)
                
        
        dis=[float('inf') for _ in range(n)]
        dis[0] = 0
        
        while stack:
            node=stack.pop()
            for child in adj[node]:
                if dis[node]+child[1]<dis[child[0]]:
                    dis[child[0]]=dis[node]+child[1]
        
        ans=[-1 for _ in range(n)]
        for i in range(n):
            if dis[i]!=float('inf'):
                ans[i] = dis[i]
        return ans
                    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends
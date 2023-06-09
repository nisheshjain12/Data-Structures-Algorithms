#User function Template for python3

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj=[[] for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        dis=[float('inf') for _ in range(n)]
        q=[]
        dis[src] = 0
        q.append(src)
        
        while q:
            node=q.pop(0)
            for child in adj[node]:
                if dis[node]+1<dis[child]:
                    dis[child] = dis[node]+1
                    q.append(child)
        
        ans=[-1 for _ in range(n)]
        for i in range(n):
            if dis[i]!=float('inf'):
                ans[i] = dis[i]
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends
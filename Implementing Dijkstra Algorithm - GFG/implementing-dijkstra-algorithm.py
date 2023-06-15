class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dis=[10**8 for _ in range(V)]
        dis[S] = 0
        pq=[]
        pq.append((S,0))
        
        while pq:
            (node,d) = pq.pop(0)
            for child,cd in adj[node]:
                if d + cd < dis[child]:
                    dis[child] = d + cd
                    pq.append((child,dis[child]))
        return dis
                    
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
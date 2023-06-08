#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        n=len(adj)
        vis=[False for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for i in range(n):
            for it in adj[i]:
                indegree[it] += 1
        q=[]
        ans=[]
        
        for i in range(n):
            if indegree[i] ==0:
                q.append(i)
        
        while q:
            node=q.pop(0)
            ans.append(node)
            
            for child in adj[node]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        
        if len(ans)==V:
            return False
        return True
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends
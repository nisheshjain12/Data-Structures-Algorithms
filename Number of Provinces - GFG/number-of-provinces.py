#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        vis=[False for _ in range(V+1)]
        
        graph={}
        
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 :
                    if i+1 not in graph:
                        graph[1+i] = []
                    graph[i+1].append(j+1)
        
        def dfs(node):
            vis[node]=True
            for child in graph[node]:
                if not vis[child]:
                    dfs(child)
        
        count=0
        for i in range(1,V+1):
            if not vis[i]:
                count+=1
                dfs(i)
                
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends
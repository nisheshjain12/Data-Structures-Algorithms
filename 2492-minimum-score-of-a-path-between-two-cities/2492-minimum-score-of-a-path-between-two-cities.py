class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=[[] for _ in range(n+1)]
        for arr in roads:
            graph[arr[0]].append([arr[1],arr[2]])
            graph[arr[1]].append([arr[0],arr[2]])
        
        mini=10**8
        
        vis=[False for _ in range(n+1)]
        
        def dfs(node):
            nonlocal mini
            vis[node] = True
           
            for child,dist in graph[node]:
                mini=min(mini,dist)
                if not vis[child]:
                    
                    dfs(child)    
                       
        dfs(1)
        return mini
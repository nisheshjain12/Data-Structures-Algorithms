class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        vis=[False for _ in range(n)]
        dfsvis=[False for _ in range(n)]
        dis=[0 for _ in range(n)]
        
        def dfs(node,distance): 
            nonlocal ans
            vis[node] = True
            dfsvis[node] = True
            
            if(edges[node] != -1):
                if not vis[edges[node]]:
                    dis[node] = distance
                    dfs(edges[node], distance+1)
                elif dfsvis[edges[node]] :
                    ans=max(ans, distance-dis[edges[node]] + 1)
            dfsvis[node] = False
    
        ans= -1
        for i in range(n):
            if not vis[i]:
                dfs(i,0)
        return ans
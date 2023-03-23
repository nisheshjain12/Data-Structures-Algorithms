class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph={}
        for i in range(n):
            graph[i] = []
        connection=0
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
            connection+=1
            
        vis = [False for _ in range(n)]
        
        def dfs(node):
            vis[node] = True
            for child in graph[node]:
                if not vis[child]:
                    dfs(child)
        
        count=0
        for i in range(n):
            if not vis[i]:
                count+=1
                dfs(i)
        
        if connection>=n-1:
            return count-1
        return -1
            
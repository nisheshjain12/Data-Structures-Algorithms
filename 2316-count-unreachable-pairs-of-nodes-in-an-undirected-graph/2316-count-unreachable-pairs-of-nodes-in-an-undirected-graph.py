class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        graph=[]
        for i in range(n):
            graph.append([])
            
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        vis=set()
        ans=0
        
        def dfs(node):
            nonlocal count
            vis.add(node)
            count+=1
            for child in graph[node]:
                if child not in vis:
                    dfs(child)
                    
        for i in range(n):
            count=0
            if i not in vis:
                dfs(i)
                print(count)
                ans+=count*(n-count)
        
        return ans//2
            
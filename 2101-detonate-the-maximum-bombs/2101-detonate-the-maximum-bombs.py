class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        
        def distance(x1,y1,x2,y2):
            ans = ((((x1-x2)**2 + (y1-y2)**2)))
            return ans

        graph={}
        for i in range(n):
            graph[i] = []

        for i in range(n):
            for j in range(n):
                if i!=j:
                    x=distance(bombs[i][0],bombs[i][1],bombs[j][0],bombs[j][1])
                    if x<=((bombs[i][2]**2)):
                        graph[i].append(j)
                    
        
        def dfs(node,val):
            vis.add(node)
            val+=1
            for child in graph[node]:
                if child not in vis:
                    dfs(child,val)

        ans=0
        for i in range(n):
            vis=set()
            val=0
            dfs(i,val)
            ans=max(ans,len(vis))

        return ans

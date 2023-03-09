class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n=len(roads)
        graph=defaultdict(list)
        
        for a,b in roads:
            graph[b].append(a)
            graph[a].append(b)
            
        
        def dfs(node,parent):
            nonlocal res
            passenger=0
            for child in graph[node]:
                if child!=parent:
                    p=dfs(child,node)
                    passenger+=p
                    res+=int(ceil(p/seats))

            return passenger+1
        res=0
        dfs(0,-1)
        return res

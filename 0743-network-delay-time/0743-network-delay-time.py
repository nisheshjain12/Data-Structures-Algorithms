import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        for i in range(n+1):
            adj[i] = []
        for u,v,w in times:
            adj[u].append((w,v))
        print(adj)
        distance=[float(inf) for _ in range(n+1)]
        pq=[(0,k)]
        heapify(pq)
        distance[k] = 0
        
        while len(pq) > 0 :
            (dis,node) = heappop(pq)
            
            for cd,child in adj[node]:
                if distance[child] > distance[node] + cd:
                    distance[child] = distance[node] + cd
                    heappush(pq,(distance[child] , child))
        
        maxi=max(distance[1:])
        return maxi if maxi!=float(inf) else -1
        
            
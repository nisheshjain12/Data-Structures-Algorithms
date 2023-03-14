class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        graph={}
        for a in arr:
            if a not in graph:
                graph[a]=1
            else:
                graph[a]+=1
     
        if len(set(graph.values())) != len(set(arr)):
            return False
        return True



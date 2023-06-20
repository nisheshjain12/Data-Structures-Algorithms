#User function Template for python3

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        dis=[float('inf') for _ in range(10**5)]
        dis[start] = 0
        q=[]
        q.append((start,0))
        
        while q:
            node,steps = q.pop(0)
            
            for it in arr:
                num = (node * it) % 100000
                if steps+1 < dis[num]:
                    dis[num] = steps+1
                    if num == end:
                        return steps+1
                    q.append(( num ,steps+1))
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends
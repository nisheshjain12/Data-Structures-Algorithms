import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        q=[]
        
        for i in range(len(nums)):
            heapq.heappush(q,(-nums[i] , i))
            
        for i in range(k):
            num,index = heapq.heappop(q)
            ans.append(index)
            
        ans.sort()
        
        res=[]
        for index in ans:
            res.append(nums[index])
        return res
        
            
        
        
        
        
            
    
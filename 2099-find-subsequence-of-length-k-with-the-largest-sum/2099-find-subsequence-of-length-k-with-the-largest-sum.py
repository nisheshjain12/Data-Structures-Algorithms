import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp=[]
        q=[]
        
        for i in range(len(nums)):
            heapq.heappush(q,nums[i])
            temp.append(nums[i])
            
        for i in range(len(nums) - k):
            temp.remove( heapq.heappop(q) )
        
        return temp

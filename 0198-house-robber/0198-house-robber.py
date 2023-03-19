class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        pre2=0
        pre1=nums[0]
        
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=pre2
            notpick=pre1
            curr=max(pick,notpick)
            pre2=pre1
            pre1=curr
        
        return pre1
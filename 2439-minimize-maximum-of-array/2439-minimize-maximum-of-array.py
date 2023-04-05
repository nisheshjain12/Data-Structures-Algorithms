class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n=len(nums)
        ans=summ=nums[0]
        
        for i in range(1,n):
            summ+=nums[i]
            ans=max(ans,math.ceil(summ/(i+1)))

        return ans
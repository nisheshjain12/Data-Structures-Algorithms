class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1 for _ in range(n)]
        
        def func(index):
            if index>=n:
                return 0
            if index==n-1:
                return nums[n-1]
            if dp[index]!=-1:
                return dp[index]
            pick=nums[index]+func(index+2)
            notpick=func(index+1)
            dp[index] = max(pick,notpick)
            return dp[index]
        
        return func(0)
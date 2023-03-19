class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1 for _ in range(n)]

        def func(i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]

            first=cost[i]+func(i+1)
            second=cost[i]+func(i+2)
            dp[i] = min(first,second)
            return dp[i]
        
        first=func(0)
        second=func(1)
        return min(first,second)
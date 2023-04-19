class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        dp=[[-1 for _ in range(2)] for i in range(n)]
        def recc(i,buy):
            if i==n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
                
            if buy:
                profit = max(-prices[i] + recc(i+1,0) , recc(i+1,1))
            else:
                profit = max(prices[i] + recc(i+1,1) , recc(i+1,0))
            dp[i][buy] = profit
            return profit
        
        return recc(0,1)
        
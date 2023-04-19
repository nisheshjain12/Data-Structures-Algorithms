class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        dp=[[-1 for _ in range(2)] for i in range(n+1)]
    
        dp[n][0] = dp[n][1] = 0
        
        for i in range(n-1,-1,-1):
            for b in range(2):
                if b:
                    profit = max(-prices[i] + dp[i+1][0] ,  dp[i+1][1])
                else:
                    profit = max(prices[i] +  dp[i+1][1] ,  dp[i+1][0])
                dp[i][b] = profit
        
        return dp[0][1]
                
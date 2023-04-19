class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        dp=[[[-1 for _ in range(k+1)]for _ in range(2)] for i in range(n)]
        def recc(i,buy,chance):
            if i==n or chance==0:
                return 0
            if dp[i][buy][chance] != -1:
                return dp[i][buy][chance]
                
            if buy:
                profit = max(-prices[i] + recc(i+1,0,chance) , recc(i+1,1,chance))
            else:
                profit = max(prices[i] + recc(i+1,1,chance-1) , recc(i+1,0,chance))
            dp[i][buy][chance] = profit
            return profit
        
        return recc(0,1,k)
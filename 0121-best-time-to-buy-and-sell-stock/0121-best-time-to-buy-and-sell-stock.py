class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        mini=prices[0]
        for i in range(len(prices)):
            cost=prices[i]-mini
            ans=max(ans,cost)
            mini=min(mini,prices[i])
        return ans
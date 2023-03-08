class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n=len(piles)
        left=0
        right=10**10

        def helper(m):
            temp=0
            for i in range(n):
                temp += (piles[i]//m + (piles[i]%m != 0))
            return temp

        while left+1<right:
            mid=(left+right)//2
            temph=helper(mid)

            if temph<=h:
                right=mid
            else:
                left=mid
        return right
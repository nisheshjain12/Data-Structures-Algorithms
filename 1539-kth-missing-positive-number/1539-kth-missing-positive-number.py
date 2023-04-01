class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        vis=set(arr)
        i=max(arr)
        ans=0
        for j in range(1,i+1+k):
            if j not in vis:
                ans=j
                k-=1
            if k==0:
                break
        return ans
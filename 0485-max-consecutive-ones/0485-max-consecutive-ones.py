class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                count=0
            maxi=max(count,maxi)
        return maxi
                
            
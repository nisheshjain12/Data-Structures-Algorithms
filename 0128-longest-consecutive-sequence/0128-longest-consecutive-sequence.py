class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vis=set(nums)
        maxi=0
        for num in nums:
            if num-1 not in vis:
                length=1
                while num+length in vis:
                    length+=1
                maxi=max(maxi,length)
        return maxi
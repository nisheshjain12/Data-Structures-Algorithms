class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l,h=0,0
        n=len(nums)
        ans=0
        while(h<n):
            if nums[h] == 0 :
                while(h<n and nums[h] == 0) :
                    h+=1
                x=h-l
                ans+=(x+1)*x//2
                l=h
            elif nums[h] != 0:
                l+=1
                h+=1
        return ans
            
            
                
            
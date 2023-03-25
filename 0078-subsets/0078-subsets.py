class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        temp=[]
        
        def rec(i):
            nonlocal temp
            if i>=n:
                ans.append(temp.copy())
                return
            
            temp.append(nums[i])
            rec(i+1)
            temp.pop()
            rec(i+1)      
        
        
        rec(0)
        return ans
            
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robin(nums):
            n=len(nums)
            pre2=0
            pre1=nums[0]

            for i in range(1,n):
                pick=nums[i]
                if i>1:
                    pick+=pre2
                notpick=pre1
                curr=max(pick,notpick)
                pre2=pre1
                pre1=curr

            return pre1
        
        n=len(nums)
        if n==1:
            return nums[0]
        temp1=[]
        temp2=[]
        
        for i in range(n):
            if i!=0:
                temp1.append(nums[i])
            if i!=n-1:
                temp2.append(nums[i])
        return max(robin(temp1),robin(temp2))
            
            
            
            
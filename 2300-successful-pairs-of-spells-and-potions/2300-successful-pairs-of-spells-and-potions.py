class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n=len(spells)
        m=len(potions)
        ans=[]
        
        potions.sort()
        
        def binary(arr,target,x):
            
            low=0
            high=len(arr)-1
            mid=(low+high)//2
            
            while low<=high:
                # if (arr[mid]*x )== target:
                #     return mid
                if (arr[mid]*x)<target:
                    low=mid+1
                else:
                    high=mid-1
                mid=(low+high)//2
            return low
                
                    
        for i in range(n):
            if potions[0] *spells[i] >= success:
                ans.append(m)
            else:
                temp = binary(potions,success,spells[i])
                ans.append(m-temp)
                      
        return ans
            
            
        
        
            
                
                
                
            
            
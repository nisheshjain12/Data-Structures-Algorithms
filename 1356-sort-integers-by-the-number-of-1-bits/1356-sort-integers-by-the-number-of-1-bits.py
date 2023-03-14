class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        dict={}
        
        def bits(n):
            count=0
            while(n>0):
                count+=(n&1)
                n=n>>1
            return count
            
        for i in range(len(arr)):
            count=bits(arr[i])
            if count not in dict:
                dict[count]=[arr[i]]
            else:
                dict[count].append(arr[i])
        print(dict)
        myKeys = list(dict.keys())
        myKeys.sort()
        ans=[]
        for i in myKeys:
            ans+=sorted(dict[i])
        return ans

        
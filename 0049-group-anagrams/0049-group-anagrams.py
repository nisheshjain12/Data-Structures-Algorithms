class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        mapp= defaultdict(list)
        
        for s in strs:
            
            temp=sorted(s)
            sortedS=''.join(temp)
            
            if sortedS not in mapp:
                mapp[sortedS] = []
                mapp[sortedS].append(s)
            else:
                mapp[sortedS].append(s)
        
        ans=[]
        for key in mapp:
            ans.append(mapp[key])
            
        return ans
                
            
        
                
                
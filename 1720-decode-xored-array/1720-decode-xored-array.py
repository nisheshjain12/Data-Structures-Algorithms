class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans=[]
        n=len(encoded)
        ans.append(first)
        for i in range(1,n+1):
            ans.append(encoded[i-1] ^ ans[i-1])
        return ans
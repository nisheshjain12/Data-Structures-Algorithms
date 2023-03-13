class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n=x^y
        count=0
        while(n>0):
            count+=(n&1)
            n=n>>1
        return count
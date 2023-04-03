class Solution:
    def isHappy(self, n: int) -> bool:
        vis=set()
        while n!=1:
            temp=n
            summ=0
            while temp:
                summ+=(temp%10)**2
                temp//=10
            n=summ
            if n in vis:
                return False
            vis.add(summ)
        return True
                
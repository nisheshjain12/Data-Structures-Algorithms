class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        q=[]
        pop=0
        for p in pushed:
            q.append(p)
            while pop<len(pushed) and q and popped[pop] == q[-1]:
                q.pop()
                pop+=1
            
                
        return True if len(q)==0 else False
                
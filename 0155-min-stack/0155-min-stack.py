class MinStack:
    
    mini=float('inf')
    
    def __init__(self):
        self.q=[]
        self.minq=[]

    def push(self, val: int) -> None:
        self.q.append(val)
        val=min(val, self.minq[-1] if self.minq else val)
        self.minq.append(val)

    def pop(self) -> None:
        self.q.pop()
        self.minq.pop()
        

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.minq[-1]
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
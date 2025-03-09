
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:
    def __init__(self):
        self.stack = list()
        self.mins = list()
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]: self.mins.append(val)
        
    def pop(self) -> None:
        if (self.stack.pop() == self.mins[-1]): self.mins.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]
        
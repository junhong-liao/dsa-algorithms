
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
Initial implementation
'''
# class MinStack:

#     def __init__(self):
#         self.stack = list()
#         self.minstack = list()
#         self.min = math.inf
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if val <= self.min:
#             self.min = val
#             self.minstack.append(val)

#     def pop(self) -> None:
#         val = self.stack.pop()
#         if self.minstack[-1] == val:
#             self.minstack.pop()
#         self.min = math.inf if not self.minstack else self.minstack[-1]
        
#     def top(self) -> int:
#         return self.stack[-1]
        
#     def getMin(self) -> int:
#         return self.min

class MinStack:
    def __init__(self):
        self.stack = list()
        self.mins = list()
        
    # if mins is empty or val is less than the smallest min so far (mins[-1]), append the val to minstack
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]: self.mins.append(val)
        
    def pop(self) -> None:
        if (self.stack.pop() == self.mins[-1]): self.mins.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]
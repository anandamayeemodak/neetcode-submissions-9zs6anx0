import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack_min.append(min(val, self.stack_min[-1]) if self.stack_min else val)
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()     
        

    def top(self) -> int:
        stack_top = self.stack[-1]
        return stack_top
        

    def getMin(self) -> int:
        return self.stack_min[-1]
        

class SpecialStack:

    def __init__(self):
        self.stack = []
    
    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            curr_min = self.stack[-1][1]
            self.stack.append((x, min(x, curr_min)))

    
    def pop(self):
        if self.stack:
            self.stack.pop()

    
    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1][0]
        
    def isEmpty(self):
        return len(self.stack) == 0

    
    def getMin(self):
        if not self.stack:
            return -1
        return self.stack[-1][1]
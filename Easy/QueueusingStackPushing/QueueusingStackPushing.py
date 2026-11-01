class myQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def enqueue(self, x):
        self.in_stack.append(x)
        
    def dequeue(self):
        self._shift_element()
        if self.out_stack:
            self.out_stack.pop()


    def front(self):
        self._shift_element()
        if not self.out_stack:
            return -1
        return self.out_stack[-1]


    def size(self):
        return len(self.out_stack) + len(self.in_stack)
        
    def _shift_element(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
class MinStack:

    def __init__(self):
        self.stack = []
        self.mi = []
        

    def push(self, val: int) -> None:
        if len(self.stack) != 0:
            self.stack.append(val)
            if self.mi[-1] > val:
                self.mi.append(val)
            else:
                self.mi.append(self.mi[-1])
        else:
            self.stack.append(val)
            self.mi.append(val)

        

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.mi = self.mi[:-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mi[-1]
        

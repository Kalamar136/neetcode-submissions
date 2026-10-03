class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum_stack:
            self.minimum_stack.append(val)
        else:
            self.minimum_stack.append(val if val < self.minimum_stack[-1] else self.minimum_stack[-1])

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minimum_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minimum_stack[-1]

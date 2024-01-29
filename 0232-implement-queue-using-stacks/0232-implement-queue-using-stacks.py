class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None
    def push(self, x: int) -> None:
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        self.front = self.stack1[-1]
        
    def pop(self) -> int:
        res = self.stack1.pop()
        if len(self.stack1):
            self.front = self.stack1[-1]
        else:
            self.front = None
            
        return res 

    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
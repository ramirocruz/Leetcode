from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.turn = 0
        
        

    def push(self, x: int) -> None:
        if(self.turn == 0):
            self.q1.append(x)
        else:
            self.q2.append(x)
        

    def pop(self) -> int:
        print(self.q1,self.q2)
        if(self.turn == 0):
            while(len(self.q1) > 1):
                tempvar = self.q1.popleft()
                self.q2.append(tempvar)
            res = self.q1.popleft()
            self.turn = 1
            print(self.q1,self.q2)
            return res
        else:
            while(len(self.q2) > 1):
                tempvar = self.q2.popleft()
                self.q1.append(tempvar)
            res = self.q2.popleft()
            self.turn = 0
            return res           

    def top(self) -> int:
        if(self.turn == 0):
            return self.q1[-1]
        else:
            return self.q2[-1]
        

    def empty(self) -> bool:
        if(self.turn == 0):
            return (len(self.q1) == 0)
        else:
            return (len(self.q2) == 0)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
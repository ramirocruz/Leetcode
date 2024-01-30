class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+","-","*","/"]:
                op2 = stack.pop()
                op1 = stack.pop()
                res = eval(op1 + t + op2)
                if t == "/":
                    res = int(res)
                # print(op1 + t + op2, res)
                stack.append(str(res))
            else:
                stack.append(t)
        
        return int(stack[0])
                
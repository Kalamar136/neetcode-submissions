class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except Exception:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == '+':
                    result = op2 + op1
                elif token == '-':
                    result = op2 - op1
                elif token == '*':
                    result = op2 * op1
                elif token == '/':
                    result = int(op2 / op1)
                stack.append(result)
        return stack.pop()
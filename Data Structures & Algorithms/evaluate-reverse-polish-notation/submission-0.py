class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['-', '+', '/', '*']
        stack = []

        for c in tokens:
            if c in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                res = 0
                if c == '-':
                    res = num2 - num1
                elif c == '+':
                    res = num2 + num1
                elif c == '*':
                    res = num2 * num1
                elif c == '/':
                    res = int(num2 / num1)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[-1]

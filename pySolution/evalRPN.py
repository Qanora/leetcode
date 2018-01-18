class Solution:
    def evalRPN(self, tokens):
        stack = []
        for val in tokens:
            if val.isdigit():
                stack.append(int(val))
            elif len(val) >= 2:
                stack.append(-int(val[1:]))
            else:
                right = stack.pop()
                left = stack.pop()
                if val == '*':
                    stack.append(left * right)
                elif val == '-':
                    stack.append(left - right)
                elif val == '+':
                    stack.append(left + right)
                else:
                    stack.append(int(left / right))
        return stack[-1]

s = Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(s)
print(int(-100/1))
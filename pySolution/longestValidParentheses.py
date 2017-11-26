class Solution:

    def longestValidParentheses(self, s):
        a = []
        for i in range(len(s)):
            if len(a) == 0:
                a.append(s[i])
                continue
            a.append(s[i])
            if (a[len(a) - 1] == ')' and isinstance(a[len(a) - 2], int)):
                for j in range(len(a) - 2, -1, -1):
                    if a[j] == '(':
                        print("pop" + str(a.pop(j)))
                        print("pop" + str(a.pop()))
                        a.append(a.pop() + 2)
                        break
                    if a[j] == ')':
                        break
            if(a[len(a) - 1] == ')' and a[len(a) - 2] == '('):
                a.pop()
                a.pop()
                a.append(2)
            if len(a) >= 2 and isinstance(a[len(a) - 1], int) and \
                    isinstance(a[len(a) - 2], int):
                a.append(a.pop() + a.pop())
        max = 0
        for i in range(len(a)):
            if (isinstance(a[i], int)) and a[i] > max:
                max = a[i]
        print(a)
        return max


s = Solution().longestValidParentheses("()(())")
print(s)

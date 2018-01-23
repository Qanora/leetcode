class Solution:
    def diffWaysToCompute(self, input):
        ans = []
        for i in range(len(input)):
            cur = input[i]
            if input[i] in ("+-*"):
                cur = input[i]
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for lval in left:
                    for rval in right:
                        if cur == '-':
                            ans.append(lval-rval)
                        elif cur == '+':
                            ans.append(lval+rval)
                        else:
                            ans.append(lval*rval)
        if not ans:
            ans.append(int(input))
        return ans

# count = 5
# while count <= 1000000:
#     print(count,bin(count))
#     count *= 5
# count = 2
# while count <= 1000000:
#     print(count,bin(count))
#     count *= 2
count = 3
while count <= 1000000:
    print(count,bin(count))
    count *= 3

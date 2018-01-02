class Solution:
    def simplifyPath(self, path):
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack: stack.pop()
            elif p and p != '.': stack.append(p)
        print("/".join(stack))
        return "/" + "/".join(stack)

Solution().simplifyPath("/home//foo/")
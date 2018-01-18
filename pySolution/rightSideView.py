import TreeNodeUtils


class Solution:
    def rightSideView(self, root):
        stack = [root]
        stack_swap = []
        ans = []
        while stack:
            temp = stack.pop(0)
            if temp.left:
                stack_swap.append(temp.left)
            if temp.right:
                stack_swap.append(temp.right)
            if not stack:
                ans.append(temp.val)
                while stack_swap:
                    stack.append(stack_swap.pop(0))
        return ans
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        stack = [root]
        quene = []
        ans = []
        while stack or quene:
            tempList = []
            while stack:
                temp = stack.pop()
                if temp.left:
                    quene.append(temp.right)
                if temp.right:
                    quene.append(temp.left)
                tempList.append(temp.val)
            if tempList:
                ans.append(tempList[:])
            tempList.clear()
            while quene:
                temp = quene.pop()
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
                tempList.append(temp.val)
            if tempList:
                ans.append(tempList[:])
            tempList.clear()
        return ans
# Definition for a  binary tree node
import TreeNodeUtils
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.ans = []
        travel = root
        while travel:
            self.ans.append(travel)
            travel = travel.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.ans) != 0

    def next(self):
        """
        :rtype: int
        """
        if self.ans:
            temp = self.ans.pop()
            if temp and temp.right:
                self.ans.append(temp.right)
                travel = temp.right
                while travel.left:
                    self.ans.append(travel.left)
                    travel = travel.left
            return temp.val


root = TreeNodeUtils.make_tree([1,2,3,4])

i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())

print(v)
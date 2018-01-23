class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        rAns = [str(root.val)]
        while stack:
            temp = stack.pop(0)
            if temp.left and temp.right:
                stack.append(temp.left)
                stack.append(temp.right)
                rAns.append(str(temp.left.val))
                rAns.append(str(temp.right.val))
            elif not temp.left and temp.right:
                stack.append(temp.right)
                rAns.append("*")
                rAns.append(str(temp.right.val))
            elif not temp.right and temp.left:
                stack.append(temp.left)
                rAns.append(str(temp.left.val))
                rAns.append("*")
            else:
                rAns.append("*")
                rAns.append("*")

        rrAns = " ".join(rAns)
        return rrAns

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        dataArr = data.split(" ")

        for i, val in enumerate(dataArr):
            if val[0] == "-":
                dataArr[i] = -int(val[1:])
            elif val == "*":
                dataArr[i] = "*"
            else:
                dataArr[i] = int(dataArr[i])

        root = TreeNode(dataArr[0])
        stack = [root]
        index = 1
        while index < len(dataArr):
            temp = stack.pop(0)
            if dataArr[index] != "*":
                temp.left = TreeNode(int(dataArr[index]))
                index += 1
                stack.append(temp.left)
            else:
                index += 1
                temp.left = None
            if index < len(dataArr) and dataArr[index] != "*":
                temp.right = TreeNode(int(dataArr[index]))
                index += 1
                stack.append(temp.right)
            else:
                index += 1
                temp.right = None
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
c = Codec()
w = c.deserialize("123 -234 3 4 5 6 7")
q = c.serialize(w)
f = c.deserialize(q)
print(w)
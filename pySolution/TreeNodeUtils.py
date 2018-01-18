class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(arr):
    if not arr:
        return None
    return dfs(arr, 0, len(arr)-1)


def dfs(arr, start, end):
    if start > end:
        return None
    mid = start + (end - start) // 2
    root = TreeNode(arr[mid])
    root.left = dfs(arr, start, mid-1)
    root.right = dfs(arr, mid+1, end)
    return root

def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)
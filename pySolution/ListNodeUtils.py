class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(arr):
    if not arr:
        print("=======Null======")
        return None
    root = ListNode(0)
    travel = root
    for val in arr:
        travel.next = ListNode(val)
        travel = travel.next
    return root.next

def print_list(root):
    if not root:
        print("=======Null======")
        return None
    travel = root
    while travel:
        print(travel.val)
        travel = travel.next
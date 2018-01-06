import ListNodeUtils

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.merge(*map(self.sortList, (head, slow)))

    # def sortList(self, head):
    #     if not head:
    #         return head
    #     stack = []
    #     travle = head
    #     while travle:
    #         stack.append(travle)
    #         travle = travle.next
    #         stack[-1].next = None
    #     while len(stack) > 1:
    #         stack.append(self.merge(stack.pop(), stack.pop()))
    #     return stack[-1]
    #
    # def merge(self, left, right):
    #     if not left and right:
    #         return right
    #     if not right and left:
    #         return left
    #     if not right and not left:
    #         return None
    #     travel_left = left
    #     travel_right = right
    #     root = ListNode(0)
    #     travel_root = root
    #     while travel_left and travel_right:
    #         if travel_left.val < travel_right.val:
    #             travel_root.next = travel_left
    #             travel_left = travel_left.next
    #         else:
    #             travel_root.next = travel_right
    #             travel_right = travel_right.next
    #         travel_root = travel_root.next
    #         travel_root.next = None
    #     travel_root.next = travel_left if travel_left else travel_right
    #     return root.next

# ans = [5,4,3,2,1]
# root = ListNodeUtils.make_list(ans)
# s = Solution().sortList(root)

ans = [1,2,3,4,5,6]
def func(a, b):
    return a+b
temp = map(func, ans)


func(1,2,3)
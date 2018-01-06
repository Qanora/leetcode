class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def reorderList(self, head):
    #     if not head:
    #         return None
    #     if not head.next:
    #         return head
    #     self.dfs(head.next, head)
    #     return head
    #
    # def dfs(self, head, first):
    #     if not head.next:
    #         first.next = head
    #         return head
    #     if head.next:
    #         temp = self.dfs(head.next, first)
    #         temp.next = head
    #         head.next= None
    #     return head
    def reorderList(self, head):
        if head and head.next:
            ans = []
            travel = head
            while travel:
                ans.append(travel)
                travel = travel.next
            l = 0
            r = len(ans) - 1
            while l < r:
                ans[l].next = ans[r]
                ans[r].next = None
                l += 1
                ans[r].next = ans[l]
                ans[l].next = None
                r -= 1


ans = [1, 2, 3, 4, 5]
root = ListNode(ans[0])
travel = root
for i in range(1, len(ans)):
    travel.next = ListNode(ans[i])
    travel = travel.next

travel = root
while travel:
    print(travel.val)
    travel = travel.next
print("===========================================")
s = Solution().reorderList(root)
travel = root
while travel:
   print(travel.val)
   travel = travel.next
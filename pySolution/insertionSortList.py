class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        root = ListNode(0)
        travel = head
        while travel:
            next = travel.next
            ruunner = root
            while ruunner.next and ruunner.next.val < travel.val:
                ruunner = ruunner.next
            travel.next = ruunner.next
            ruunner.next = travel

            travel = next
        return root.next



ans = [1,1]
root = ListNode(ans[0])
travel = root
for val in ans[1:]:
    temp = ListNode(val)
    travel.next = temp
    travel = travel.next

travel = root
while travel:
    print(travel.val)
    travel = travel.next
print("=============================================")
s = Solution().insertionSortList(root)

travel = s
while travel:
    print(travel.val)
    travel = travel.next
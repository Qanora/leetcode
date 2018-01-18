import ListNode

class Solution:
    def removeElements(self, head, val):
        root = ListNode(0)
        root.next = head
        travel = root
        while travel.next:
            if travel.next.val == val:
                travel.next = travel.next.next
            travel = travel.next
        return root.next
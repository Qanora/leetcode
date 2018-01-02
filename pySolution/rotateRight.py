class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def rotateRight(self, head, k):
        travel = head
        count = 1
        totalCount = -1
        new_head = head
        while travel:
            if travel.next == None:
                travel.next = head
                totalCount = count
                if totalCount < k:
                    k = k % totalCount
            if count == totalCount*2 - k:
                new_head = travel.next
                travel.next = None
                break
            travel = travel.next
            count += 1
        return new_head

head = ListNode(1)
travel = head
"""for i in range(2,6):
    travel.next = ListNode(i)
    travel = travel.next"""
s = Solution().rotateRight(head,99)
travel = s
while travel:
    print(travel.val)
    travel = travel.next
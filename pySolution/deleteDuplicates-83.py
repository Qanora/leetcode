class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        travel = head
        while travel:
            while travel.next and travel.val == travel.next.val:
                travel.next = travel.next.next
            travel = travel.next
        return head

List = [1,1,1,3,3]
head = ListNode(List[0])
travel = head
for val in List[1:]:
    temp = ListNode(val)
    travel.next = temp
    travel = travel.next

travel = head
while travel:
    print(travel.val)
    travel = travel.next

s = Solution().deleteDuplicates(head)
travel = s
while travel:
    print(travel.val)
    travel = travel.next

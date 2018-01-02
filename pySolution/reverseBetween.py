class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        newHead = ListNode(None)
        newHead.next = head
        reverseHead = ListNode(None)
        count = 0
        travel = newHead

        while count < m - 1:
            travel = travel.next
            count += 1
        reverseHead = travel.next
        while count < n:
            travel.next = travel.next.next
            count += 1

        travel = newHead
        count = 0
        newTravel = reverseHead
        while count < m - 1:
            travel = travel.next
            count += 1
        count = 0
        while newTravel and count < n - m + 1:
            temp = ListNode(newTravel.val)
            temp.next = travel.next
            travel.next = temp
            count += 1
            newTravel = newTravel.next

        return newHead.next
List = [1,2,3,4,5]
head = ListNode(List[0])
travel = head
for val in List[1:]:
    temp = ListNode(val)
    travel.next = temp
    travel = travel.next

#travel = head
#while travel:
#    print(travel.val)
#    travel = travel.next

s = Solution().reverseBetween(head,1,5)
#travel = s
#while travel:
#    print(travel.val)
#    travel = travel.next

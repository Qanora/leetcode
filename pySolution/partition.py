class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head, x):
        if not head:
            return []
        greatHead = ListNode(None)
        lessHead = ListNode(None)

        lessTravel = lessHead
        greatHead.next = head

        greatTravel = greatHead

        while greatTravel:
            if greatTravel.next and greatTravel.next.val < x:
                lessTravel.next = greatTravel.next
                greatTravel.next = greatTravel.next.next
                lessTravel = lessTravel.next
                lessTravel.next = None
            else:
                greatTravel = greatTravel.next

        #if not greatHead.next:
        #    return lessHead.next
        travel = lessHead
        while travel.next:
            travel = travel.next
        travel.next = greatHead.next

        return lessHead.next


List = [1,4,3,2,5,2]
head = ListNode(List[0])
travel = head
for val in List[1:]:
    temp = ListNode(val)
    travel.next = temp
    travel = travel.next

travel = head
while travel:
    travel = travel.next

s = Solution().partition(head,3)
travel = s
while travel:
    print(travel.val)
    travel = travel.next




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        travel = head
        if head:
            return []
        headFlag = False
        newHead = head
        while travel:
            nextTravel = travel.next
            if not nextTravel:
                break
            inTravel = nextTravel.next
            if not inTravel:
                if headFlag:
                    newHead = nextTravel
                    headFlag = False
                break
            if travel.val == nextTravel.val:
                headFlag = True
            if nextTravel.val == inTravel.val:
                travel.next = inTravel.next
                nextTravel = inTravel.next
                if nextTravel:
                    inTravel = nextTravel.next
                else:
                    break
            else:
                travel = travel.next
                if headFlag:
                    newHead = travel.next
                    headFlag = False
        if travel.next:
            return travel
        if headFlag or travel.val == travel.next.val:
            return []
        return newHead

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

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy
        while curr:
            has_dup = False
            # Remove duplicates and leave the last of the duplicates.
            while curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
                has_dup = True
            if has_dup:
                # Remove the last duplicate
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
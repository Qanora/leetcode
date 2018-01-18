
import ListNodeUtils
class Solution:
    def getIntersectionNode(self, headA, headB):
        travelA = headA
        travelB = headB

        while travelA != travelB:

            travelA = travelB if not travelA else travelA.next
            travelB = travelA if not travelB else travelB.next

        return travelA

a = ListNodeUtils.make_list([1,2])
b = ListNodeUtils.make_list([3])
c = Solution().getIntersectionNode(a,b)
print(None == None)

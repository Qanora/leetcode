import ListNodeUtils

class Solution:
    def reverseList(self, head):
        self.newHead = None
        self.reverse(head)
        return self.newHead

    def reverse(self, head):
        if not head.next or not head:
            self.newHead = head
            return head
        self.reverse(head.next).next = head
        head.next = None
        return head

t = ListNodeUtils.make_list([1,2,3])
s = Solution().reverseList(t)
ListNodeUtils.print_list(s)
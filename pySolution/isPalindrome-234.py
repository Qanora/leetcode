import ListNodeUtils
class Solution:
    def isPalindrome(self, head):
        if not head:
            return False
        s = self.depth(head.next, head)
        if s:
            return True
        return False


    def depth(self, rhead, head):
        if rhead :
            head = self.depth(rhead.next, head)
            if head and rhead.val == head.val:
                print(rhead.val, head.val)
                return head.next
            return
        return head
s = ListNodeUtils.make_list([1,3,1,3,1])
w = Solution().isPalindrome(s)
print(w)

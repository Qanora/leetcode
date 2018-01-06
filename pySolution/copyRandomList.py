class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        root = RandomListNode(head.label)
        travel_root = root
        travel = head.next
        Mappping = {}
        Mappping[head] = root

        while travel:
            travel_root.next = RandomListNode(travel.label)
            Mappping[travel] = travel_root.next
            travel_root = travel_root.next
            travel = travel.next

        travel_root = root
        travel = head

        while travel:
            travel_root.random = Mappping.get(travel.random)
            travel_root = travel_root.next
            travel = travel.next
        return root

ans = [1, 2, 2, 2]
root = RandomListNode(ans[0])
travel = root
for i in range(1, len(ans)):
    travel.next = RandomListNode(ans[i])
    travel = travel.next
travel = root
while travel:
    print(travel.label)
    travel = travel.next
print("===========================================")
s = Solution().copyRandomList(root)
travel = s
while travel:
    print(travel.label)
    travel = travel.next
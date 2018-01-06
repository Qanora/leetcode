class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity):
        self.left = None
        self.right = None
        self.length = capacity
        self.index = 0
        self.dict = {}

    def get(self, key):
        if key not in self.dict:
            return -1
        else:
            self.upgrade(key)
            return self.dict[key].value

    def put(self, key, value):
        if key not in self.dict:
            self.dict[key] = ListNode(key, value)
            if self.index < self.length or self.length == 1:
                if not self.left or self.length == 1:
                    if self.length == 1 and self.left:
                        self.dict.pop(self.left.key)
                    self.left = self.dict[key]
                elif not self.right:
                    self.right = self.dict[key]
                    self.left.next= self.right
                    self.right.pre= self.left
                else:
                    self.right.next = self.dict[key]
                    self.dict[key].pre = self.right
                    self.right = self.dict[key]
            elif not self.right:
                self.right = self.dict[key]
                self.left.next = self.right
                self.right.pre = self.left
            else:
                self.dict.pop(self.left.key)
                self.left = self.left.next
                self.left.pre = None
                self.right.next = self.dict[key]
                self.dict[key].pre = self.right
                self.right = self.dict[key]
        else:
            self.upgrade(key)
            self.dict[key].value = value
        self.index += 1

    def upgrade(self, key):
        if not self.right or self.dict[key] == self.right:
            return
        elif self.dict[key] == self.left:
            if self.left.next == self.right:
                self.left = self.right
                self.right.pre = None
                self.right = self.dict[key]
                self.right.next = None
                self.left.next = self.right
                self.right.pre = self.left
            else:
                self.left = self.left.next
                self.left.pre = None
                self.right.next = self.dict[key]
                self.dict[key].pre = self.right
                self.right = self.dict[key]
                self.right.next = None
        else:
            self.dict[key].pre.next = self.dict[key].next
            self.dict[key].next.pre = self.dict[key].pre
            self.right.next = self.dict[key]
            self.dict[key].pre = self.right
            self.right = self.dict[key]
            self.right.next = None



order = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
para = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

s = None
for i in range(len(order)):
    if i == 40:
        a = 5
    if order[i] == "LRUCache":
        s = LRUCache(para[i][0])
    if order[i] == "put":
        s.put(para[i][0], para[i][1])
    if order[i] == "get":
        print(s.get(para[i][0]))


"""["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]"""


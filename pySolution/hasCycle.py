class Solution:
    def hasCycle(self, head):
        runner = head
        worker = head
        while runner.next and runner.next.next:
            worker = worker.next
            runner = runner.next.next
            if worker == runner:
                return True
        return False
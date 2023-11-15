from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        while head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return curr


node5 = ListNode(3, None)
node4 = ListNode(3, node5)
node3 = ListNode(2, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)

Solution().deleteDuplicates(node1)
node = node1
while True:
    if node.next:
        print(node.val)
        node = node.next
    else:
        print(node.val)
        break

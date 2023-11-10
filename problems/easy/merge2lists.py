# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: None | ListNode
    ) -> ListNode | None:
        print(list1.val, list1.next.val, list1.next.next.val)

        while not None:
            list1


list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(1, ListNode(5, ListNode(6)))
s = Solution().mergeTwoLists(list1, list2)

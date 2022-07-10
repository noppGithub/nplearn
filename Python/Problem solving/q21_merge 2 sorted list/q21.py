from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class Solution(object):
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = dummy = ListNode(None)
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 or list2
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    print(s.mergeTwoLists(ListNode([1, 2, 4]), ListNode([1, 3, 4])))

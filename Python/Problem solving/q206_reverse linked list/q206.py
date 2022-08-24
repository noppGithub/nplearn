from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return (
            "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
        )


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the input data is empty, return None
        if not head:
            return None
        # if the ListNode has only one element, return the same element
        if not head.next:
            return head

        # if the ListNode has more than one element, reverse the ListNode
        # loop each item in the list
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


# helper function to create linked list
def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))


if __name__ == "__main__":
    s = Solution()
    listnode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    x = s.reverseList(listnode)
    print(x)

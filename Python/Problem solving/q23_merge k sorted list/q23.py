import heapq
from typing import List, Optional


# ================================= If it's Linked List =================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # ================================= The solution that I really have no idea about =================================
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        curr = head = ListNode(0)
        queue = []
        count = 0
        for l in lists:
            if l is not None:
                count += 1
                heapq.heappush(queue, (l.val, count, l))
        while len(queue) > 0:
            _, _, curr.next = heapq.heappop(queue)
            curr = curr.next
            if curr.next is not None:
                count += 1
                heapq.heappush(queue, (curr.next.val, count, curr.next))
        return head.next


# ================================= If it's just a list =================================
class SolutionSimpleList:
    def mergeKLists(self, lists: List[List[int]]) -> List:
        output = []
        for lst in lists:
            output.extend(lst)
        output.sort()
        return output

    def order_by_heap(self,lists:List[List[int]])-> List:
        h = []
        for lst in lists:
            for value in lst:
                heapq.heappush(h, value)
        return [heapq.heappop(h) for i in range(len(h))]

# ================================= Helper function =================================
def list_to_linkedlist(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_linkedlist(arr[1:]))

# ================================= Run the test =================================
if __name__ == "__main__":
    # Simple List, we can use heap for this as well
    s = SolutionSimpleList()
    my_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(s.mergeKLists(my_list))
    print(s.order_by_heap(my_list))

    # Linked List
    item1 = ListNode(1, ListNode(4, ListNode(5)))
    item2 = ListNode(1, ListNode(3, ListNode(4)))
    item3 = ListNode(2, ListNode(6))

    # Linked list using function
    ll1 = list_to_linkedlist([1, 4, 5])
    ll2 = list_to_linkedlist([1, 3, 4])
    ll3 = list_to_linkedlist([2, 6])
    s = Solution()
    print(s.mergeKLists([ll1, ll2, ll3]))

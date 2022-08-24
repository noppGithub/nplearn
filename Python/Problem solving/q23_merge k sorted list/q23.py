import heapq
from typing import List, Optional


# ================================= If it's Linked List =================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


class Solution:
    # ================================= The solution that use heap/priority queue =================================
    def mergeKLists_heap(
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

    # ================================= The solution that understandable =================================
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_list = []
            
            # iterate with step 2 for merging
            for i in range(0,len(lists),2):
                list1 = lists[i]
                
                # check if we have list2 in the input
                if len(lists) > (i+1):
                    list2 = lists[i+1]
                else:
                    list2 = None
                
                # merge 2 lists
                merged_list.append(self.merge_2_list(list1,list2))
            lists = merged_list
        return lists[0]

    def merge_2_list(self,list1,list2):
        # dummy for avoiding empty linked list, it will store value when assign something to prev, not prev.next
        # prev is for ensure the lowest of 2 list keep connecting
        prev = dummy = ListNode()

        # iterate over 2 lists
        while list1 and list2:
            print(f"Value of first item are: {list1.val} vs {list2.val}")
            if list1.val < list2.val:
                prev.next = list1 #append the list to the prev and dummy
                list1 = list1.next #remove the first/lowest from the list 1
            else:
                prev.next = list2 #append the list to the prev and dummy
                list2 = list2.next #remove the first/lowest from the list2
            prev = prev.next #remove the first item from the prev only, not dummy
            print(f"After loop the value of prev and dummy are")
            print(f"prev: {prev}")
            print(f"dummy: {dummy}")
        # if any list still have value, add them to the tail
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
        return dummy.next

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
    # a helper function for creating  linkedlist from list
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

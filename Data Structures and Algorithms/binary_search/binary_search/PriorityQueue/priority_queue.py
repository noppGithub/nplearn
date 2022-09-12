# You want to implement a queue that sorts items by a given priority and always returns
# the item with the highest priority on each pop operation.
# ref: https://github.com/dabeaz/python-cookbook/blob/master/src/1/implementing_a_priority_queue/example.py
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# Example use
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item("foo"), 1)
    q.push(Item("bar"), 5)
    q.push(Item("spam"), 4)
    q.push(Item("grok"), 1)

    print("Should be bar:", q.pop())
    print("Should be spam:", q.pop())
    print("Should be foo:", q.pop())
    print("Should be grok:", q.pop())

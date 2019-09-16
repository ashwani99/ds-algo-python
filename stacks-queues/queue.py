# simple implementation, but expensive dequeue operation => O(n)
class Queue:
    def __init__(self, buffer_size):
        self.buffer = []

    def enqueue(self, data):
        self.buffer.append(data)

    def dequeue(self, data):
        return self.buffer.pop(0)

    @property
    def is_empty(self):
        return self.buffer == []


# implementation using collections.deque

from collections import deque

class Queue2:
    def __init__(self):
        self._buffer = deque()

    def enqueue(self, data):
        self._buffer.append(data)

    def dequeue(self):
        return self._buffer.popleft()


if __name__ == '__main__':
    q = Queue2()
    print(q)
    q.enqueue(7)
    q.enqueue(8)
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue() # raises IndexError: cannot remove from empty queue

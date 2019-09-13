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


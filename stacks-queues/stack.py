class Stack:
    def __init__(self, maxsize):
        self.elements = []
        self.current_size = 0
        self.maxsize = maxsize

    def push(self, data):
        if self.current_size == self.maxsize:
            raise Exception('Stack is already full. Cannot insert element.')
        self.elements.append(data)
        self.current_size += 1

    def pop(self):
        if self.is_empty:
            raise Exception('Cannot pop element from empty stack')
        self.current_size -= 1
        popped = self.elements[-1]
        del self.elements[-1]
        return popped

    def top(self):
        if self.is_empty:
            raise Exception('Cannot get top element from empty stack')
        return self.elements[-1]

    @property
    def is_empty(self):
        return self.current_size == 0


if __name__ == '__main__':
    s = Stack(5)
    
    # push some elements into the stack
    s.push(2)
    s.push(23)
    s.push(12)

    # print top element
    print(s.top()) # should print 12

    # check if stack is empty
    print('Stack is empty') if s.is_empty else print('Stack is not empty')

    # pop some elements from the stack
    s.pop() # 12 popped
    popped_element = s.pop() # should return 23
    print(s.top()) # 2
    s.pop()

    s.pop() # raises exception

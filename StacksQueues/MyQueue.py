from collections import deque


class MyQueue():
    def __init__(self):
        self.queue = deque()
        self.first = None
        self.last = None
        self.length = 0

    def update(self):
        if self.length > 0:
            self.first = self.queue[0]
            self.last = self.queue[-1]
        else:
            self.first = None
            self.last = None

    def peek(self):
        return self.first

    def enqueue(self, value):
        self.queue.append(value)
        self.length += 1
        self.update()

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('dequeue from empty queue')
        re_value = self.queue.popleft()
        self.length -= 1
        self.update()
        return re_value

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def __str__(self):
        return str(self.queue)

    __repr__ = __str__


if __name__ == "__main__":
    queue = MyQueue()
    try:
        queue.dequeue()
    except IndexError as e:
        print(e)
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(8)
    assert queue.dequeue(), 2
    assert queue.peek(), 4
    print(queue.first)
    print(queue.last)
    print(queue)

from collections import deque


class MyStackLL():
    def __init__(self):
        self.stack = deque()
        self.top = None
        self.bottom = None
        self.length = 0

    def update(self):
        if self.length > 0:
            self.top = self.stack[-1]
            self.bottom = self.stack[0]
        else:
            self.top = None
            self.bottom = None

    def peek(self):
        return self.top

    def push(self, value):
        self.stack.append(value)
        self.length += 1
        self.update()

    def pop(self):
        if self.isEmpty():
            raise IndexError('pop from empty stack')
        self.length -= 1
        top = self.stack.pop()
        self.update()
        return top

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def __str__(self):
        return str(self.stack)

    __repr__ = __str__


if __name__ == "__main__":
    stack = MyStackLL()
    try:
        stack.pop()
    except IndexError as e:
        print(e)
    stack.push(2)
    stack.push(4)
    stack.push(6)
    stack.push(8)
    assert stack.pop(), 8
    assert stack.peek(), 6
    print(stack.top)
    print(stack.bottom)
    print(stack)

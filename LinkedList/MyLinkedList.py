class MyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def newNode(self, value, next: dict = None) -> dict:
        return {'value': value, 'next': next}

    # If it is empty, init the LL and return True
    def initIfEmpty(self, value):
        if self.length == 0:
            self.head = self.newNode(value)
            self.tail = self.head
            self.length += 1
            return True
        return False

    def append(self, value) -> None:
        if self.initIfEmpty(value):
            return
        new_tail = self.newNode(value)
        self.tail['next'] = new_tail
        self.tail = new_tail
        self.length += 1

    def prepend(self, value) -> None:
        if self.initIfEmpty(value):
            return
        new_head = self.newNode(value, self.head)
        self.head = new_head
        self.length += 1

    def lookup(self, index: int) -> dict:
        if index >= self.length:
            raise IndexError('linked list index out of range')
        current_node = self.head
        for i in range(index):
            current_node = current_node['next']
        return current_node

    def insert(self, index: int, value) -> None:
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return

        previous_to_new_node = self.lookup(index - 1)
        original_node = previous_to_new_node['next']
        new_node = self.newNode(value, original_node)
        previous_to_new_node['next'] = new_node
        self.length += 1

    def remove(self, index: int) -> None:
        if index >= self.length:
            raise IndexError('linked list index out of range')
        if self.length == 1:  # Remove the only node
            self.__init__()
            return
        if index == 0:  # Remove head.
            self.head = self.head['next']
            return
        previous_to_deleted_node = self.lookup(index - 1)
        deleted_node = previous_to_deleted_node['next']
        previous_to_deleted_node['next'] = deleted_node['next']
        if index == self.length - 1:  # Remove tail and set new tail.
            self.tail = previous_to_deleted_node
        self.length -= 1

    def reverse(self):
        if self.length == 1:
            return
        # Get all nodes
        nodes = self.getAllNodes()
        self.head = self.newNode(nodes[0])
        for node in nodes[1:]:
            self.prepend(node)

    # From the course. This solution is about 4 times faster than mine
    def reverse2(self):
        if self.length == 1:
            return
        # [7, 10, 5, 16]
        first = self.head
        self.tail = self.head
        second = first['next']
        while second:
            temp = second['next']
            second['next'] = first
            first = second
            second = temp
        self.head['next'] = None
        self.head = first

    def getAllNodes(self):
        nodes_values = []
        current_node = self.head
        while current_node['next'] is not None:
            nodes_values.append(current_node['value'])
            current_node = current_node['next']
        nodes_values.append(current_node['value'])  # Add the last node's value
        return nodes_values

    def __str__(self):
        if self.length == 0:
            return str('[]')
        return str(self.getAllNodes())

    __repr__ = __str__


if __name__ == "__main__":
    my_ll = MyLinkedList()
    my_ll.append(10)
    my_ll.append(5)
    my_ll.append(16)
    my_ll.prepend(7)
    print(my_ll)
    print('length', my_ll.length)
    print('lookup index 2:', my_ll.lookup(2))
    my_ll.insert(4, 666)
    print(my_ll, '\n', my_ll.head, '\ntail', my_ll.tail)
    my_ll.remove(4)
    print(my_ll, '\n', my_ll.head, '\ntail', my_ll.tail)
    my_ll.reverse2()
    print('\n', my_ll, '\n', my_ll.head, '\n', my_ll.tail)

    # Test which reverse method is more efficient
    import timeit
    test_reverse1 = "my_ll.reverse()"

    test_reverse2 = "my_ll.reverse2()"
    setup_code = """
from __main__ import MyLinkedList
my_ll = MyLinkedList()
my_ll.append(10)
my_ll.append(5)
my_ll.append(16)
my_ll.prepend(7)
"""
    reverse_time = timeit.repeat(test_reverse1, setup_code, repeat=3)
    reverse2_time = timeit.repeat(test_reverse2, setup_code, repeat=3)
    print(f"Minimum execution time for reverse is {min(reverse_time)}")
    print(f"Minimum execution time for reverse2 is {min(reverse2_time)}")

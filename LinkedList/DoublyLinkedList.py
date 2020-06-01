class MyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def newNode(self, value, prev_node: dict = None,
                next_node: dict = None) -> dict:
        return {'value': value, 'prev': prev_node, 'next': next_node}

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
        new_tail = self.newNode(value, prev_node=self.tail)
        self.tail['next'] = new_tail
        self.tail = new_tail
        self.length += 1

    def prepend(self, value) -> None:
        if self.initIfEmpty(value):
            return
        new_head = self.newNode(value, None, self.head)
        self.head['prev'] = new_head
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
        new_node = self.newNode(value, prev_node=previous_to_new_node,
                                next_node=original_node)
        original_node['prev'] = new_node
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
            self.head['prev'] = None
            return
        if index == self.length - 1:  # Remove the tail is easier in Doubly LL
            self.tail = self.tail['prev']
            self.tail['next'] = None
            return
        previous_to_deleted_node = self.lookup(index - 1)
        deleted_node = previous_to_deleted_node['next']
        next_to_deleted_node = deleted_node['next']
        # If we are deleting the last node
        if next_to_deleted_node is not None:
            previous_to_deleted_node['next'] = next_to_deleted_node
            next_to_deleted_node['prev'] = previous_to_deleted_node
        else:
            previous_to_deleted_node['next'] = None
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
    print(my_ll)
    my_ll.append(10)
    my_ll.append(5)
    my_ll.append(16)
    my_ll.prepend(7)
    print(my_ll.head)
    print(my_ll)
    print('length', my_ll.length)
    print('lookup index 2:', my_ll.lookup(2))
    my_ll.insert(4, 666)
    print(my_ll, '\n\n', my_ll.head, '\n\ntail', my_ll.tail)
    my_ll.remove(4)
    print(my_ll, '\n\n', my_ll.head, '\n\ntail', my_ll.tail)
    print('\n\n', my_ll.head['next']['next']['prev'])
    my_ll.reverse()
    print('\n', my_ll, '\n', my_ll.head)

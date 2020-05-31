# This is a simple hash table implementation using a basic hash function
# that only supports string as key


class MyHashTable():
    def __init__(self, size: int = 59):
        if type(size) != int:
            raise TypeError('Size must be an integer')
        self.size = size
        self.table = [None for i in range(size)]

    # This hash function is from the course
    # It will generate many collision results
    def _Myhash(self, key):
        # return sum(bytearray(str(key), 'utf-8')) % self.size
        key = str(key)
        re_hash = 0
        for i in range(len(key)):
            re_hash = (re_hash + sum(key[i].encode()) * i) % self.size
        return re_hash

    def getValue(self, key):
        key = str(key)
        address = self._Myhash(key)
        key_value_pairs = self.table[address]
        if key_value_pairs is None:
            raise KeyError(f'{key}')
        for pair in key_value_pairs:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f'{key}')

    def setValue(self, key, value):
        key = str(key)
        address = self._Myhash(key)
        # If no collision
        # We can use LL to solve collision by the way because
        # LL has faster insertion and deletion.
        if self.table[address] is None:
            self.table[address] = []
        self.table[address].append([key, value])

    def loopitems(self):
        items = []
        for item in self.table:
            if item:
                for pair in item:
                    items.append(pair)
        return items

    def keys(self):
        items = self.loopitems()
        keys = []
        for pair in items:
            keys.append(pair[0])
        return keys

    def items(self):
        return self.loopitems()


if __name__ == "__main__":
    ht1 = MyHashTable(2)
    {'apples': 1000, 'bananas': 2000, 'oranges': 3000}
    ht1.setValue('apples', 1000)
    ht1.setValue('bananas', 2000)
    ht1.setValue('oranges', 3000)
    print(ht1.table)
    print(ht1.getValue('bananas'))
    print(ht1.getValue('oranges'))
    print(ht1.keys())
    print(ht1.items())
    # print(ht1.getValue('strawberries'))

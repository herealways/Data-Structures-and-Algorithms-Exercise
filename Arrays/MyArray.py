class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index: int):
        if type(index) != int:
            raise TypeError
        return self.data[index]

    def push(self, value) -> None:
        self.data[self.length] = value
        self.length += 1

    def pop(self) -> None:
        self.data.pop(self.length - 1)
        self.length -= 1

    def insert(self, index: int, value) -> None:
        self.ShiftItems(index, value)

    def delete(self, index: int) -> None:
        self.ShiftItems(index)

    def ShiftItems(self, index: int, insert_value=None) -> None:
        if index < 0 or index >= self.length:
            raise IndexError
        if insert_value:
            # insert
            self.length += 1
            for i in range(self.length - 1, index - 1, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = insert_value
        else:
            # delete
            self.data.pop(index)
            self.length -= 1
            for i in range(index, self.length):
                self.data[i] = self.data[i + 1]

    def __str__(self):
        print_str = '['
        for i in range(self.length):
            print_str += f'{self.data[i]}, '
        print_str = print_str[:-2]
        print_str += ']'
        return print_str

    __repr__ = __str__


if __name__ == "__main__":
    arr = MyArray()
    arr.push('a')
    arr.push('b')
    arr.push('c')
    arr.push('d')
    arr.push(',')
    print(arr)
    print(arr.get(2))
    arr.pop()
    arr.insert(2, 2)
    print(arr)
    arr.delete(2)
    print(arr)
    arr.delete(3)
    print(arr)
    arr.insert(2, 3)
    print(arr)

def heapify(numbers: list, length: int, root_index: int):
    largest = root_index
    left = root_index * 2 + 1
    right = root_index * 2 + 2

    # If root node has left child and its value is bigger than root
    if left < length and numbers[largest] < numbers[left]:
        largest = left
    if right < length and numbers[largest] < numbers[right]:
        largest = right
    # Swap nodes
    if root_index != largest:
        numbers[root_index], numbers[largest] =\
            numbers[largest], numbers[root_index]
        # Do checks after swapping
        heapify(numbers, length, largest)


def heapSort(numbers: list):
    length = len(numbers)
    # Build a maxheap
    # length//2 - 1: Check all the parent nodes
    for i in range(length//2 - 1, -1, -1):
        heapify(numbers, length, i)

    end_index = length - 1
    # Repeatedly extract root node
    for i in range(length):
        numbers[0], numbers[end_index] = numbers[end_index], numbers[0]
        heapify(numbers, end_index, 0)
        end_index -= 1


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    heapSort(numbers)
    print(numbers)

def selectionSort(numbers):
    length = len(numbers)
    if length == 1:
        return numbers
    for i in range(length):
        smallest = numbers[i]
        for j in range(i, length):
            if numbers[j] < smallest:
                smallest = numbers[j]
                smallest_index = j
        temp = numbers[i]
        numbers[i] = smallest
        numbers[smallest_index] = temp
    return numbers


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(selectionSort(numbers))

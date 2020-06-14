def insertionSort(numbers):
    for i in range(len(numbers)):
        current_item = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > current_item:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = current_item
    return numbers

# e.g.
# 44 99 6
# 44 99 99
# 44 44 99
# 6 44 99


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(insertionSort(numbers))

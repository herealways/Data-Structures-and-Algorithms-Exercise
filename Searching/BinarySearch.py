def binarySearch(numbers: list, number: int) -> int:
    length = len(numbers)
    left = 0
    right = length - 1
    while True:
        if left > right:
            return -1  # Not found
        middle = (left + right) // 2
        if numbers[middle] < number:
            left = middle + 1
        elif numbers[middle] > number:
            right = middle - 1
        else:
            return middle


if __name__ == "__main__":
    numbers = [1, 2, 5, 6, 7, 12, 15, 18, 23, 26, 29, 31, 35, 48, 52, 79]
    print(binarySearch(numbers, 15))
    print(binarySearch(numbers, 88))
    numbers2 = []

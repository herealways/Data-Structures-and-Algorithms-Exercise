def quickSort(numbers: list, low: int, high: int) -> None:
    if high - low < 1:
        return
    pivot_index = high  # Pick the last item as pivot
    pivot = numbers[pivot_index]
    # Partition
    i = 0
    while i < high:
        """When i > index, it means all elements greater than pivot has been
        placed to the right of pivot."""
        if i > pivot_index:
            break
        if numbers[i] > numbers[pivot_index]:
            """Swap numbers[i] and numbers[pivot_index - 1].
            Then swap numbers[pivot_index] and numbers[pivot_index - 1].
            Therefore, elements greater than pivot will be placed at the
            right of pivot. Finally update pivot_index"""
            # numbers[i], numbers[pivot_index - 1] =\
            #     numbers[pivot_index - 1], numbers[i]
            temp = numbers[i]
            numbers[i] = numbers[pivot_index - 1]
            numbers[pivot_index - 1] = temp

            numbers[pivot_index] = numbers[pivot_index - 1]
            numbers[pivot_index - 1] = pivot
            pivot_index -= 1
        else:
            i += 1
    quickSort(numbers, low, pivot_index - 1)
    quickSort(numbers, pivot_index + 1, high)


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    quickSort(numbers, 0, len(numbers) - 1)
    print(numbers)
    import timeit
    setup_code = 'from __main__ import quickSort, numbers'
    test_code1 = 'quickSort(numbers, 0, len(numbers) - 1)'
    time1 = timeit.repeat(test_code1, setup_code, number=100000)
    print('My implementation:', min(time1))

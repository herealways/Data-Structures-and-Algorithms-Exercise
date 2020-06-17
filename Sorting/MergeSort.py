def mergeSort(numbers: list) -> list:
    length = len(numbers)
    if length == 1:
        return numbers
    # Split the array into 2 halves
    half_length = length // 2
    left = numbers[:half_length]
    right = numbers[half_length:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    sorted_numbers = []  # not-in-place or out-of-space
    i = j = 0  # index for left and right
    len_left = len(left)
    len_right = len(right)
    # Compare and sort numbers
    while i < len_left and j < len_right:
        if left[i] < right[j]:
            sorted_numbers.append(left[i])
            i += 1
        else:
            sorted_numbers.append(right[j])
            j += 1
    if i >= len_left:
        sorted_numbers += right[j:]
    else:
        sorted_numbers += left[i:]

    return sorted_numbers


def mergeSort2(arr):  # From https://www.geeksforgeeks.org/merge-sort/
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort2(L)  # Sorting the first half
        mergeSort2(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    setup_code = 'from __main__ import mergeSort, mergeSort2, numbers'
    test_code1 = 'mergeSort(numbers)'
    test_code2 = 'mergeSort2(numbers)'
    import timeit
    time1 = timeit.repeat(test_code1, setup_code, number=100000)
    time2 = timeit.repeat(test_code2, setup_code, number=100000)
    print('My implementation:', min(time1))
    print('Implementation from geeksforgeeks', min(time2))

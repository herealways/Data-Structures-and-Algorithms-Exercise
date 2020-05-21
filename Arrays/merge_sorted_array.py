# Input: [0, 3, 4, 31] [4, 6, 30]
# Output: [0, 3, 4, 4, 6, 30, 31]


def MergeSortedArrays(arr1: list, arr2: list) -> list:
    merged_array = []
    # Which array is larger, and the length of the 2 arrays
    if len(arr1) >= len(arr2):
        larger_arr = arr1
        smaller_arr = arr2
    else:
        larger_arr = arr2
        smaller_arr = arr1
    larger_arr_len = len(larger_arr)
    smaller_arr_len = len(smaller_arr)
    if smaller_arr_len == 0:  # Check input
        return larger_arr

    biggest_num = None
    for i in range(larger_arr_len):
        item1 = larger_arr[i]
        if not biggest_num:
            biggest_num = item1
        elif item1 > biggest_num:
            merged_array.append(biggest_num)
            biggest_num = item1
        else:
            merged_array.append(item1)

        if i >= smaller_arr_len:
            continue
        item2 = smaller_arr[i]
        if item2 > biggest_num:
            merged_array.append(biggest_num)
            biggest_num = item2
        else:
            merged_array.append(item2)
    merged_array.append(biggest_num)
    return merged_array


def MergeSortedArrays2(arr1, arr2):
    merged_array = arr1 + arr2
    merged_array.sort()
    return merged_array


def MergeSortedArrays3(arr1, arr2):
    # Check input
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    merged_array = []
    arr1_item = arr1[0]
    arr2_item = arr2[0]
    i = j = 1
    while arr1_item | arr2_item:
        if arr1_item > arr2_item:
            merged_array.append(arr2_item)
            try:
                arr2_item = arr2[i]
            except IndexError:
                arr2_item = None
                break
            i += 1
        else:
            merged_array.append(arr1_item)
            try:
                arr1_item = arr1[j]
            except IndexError:
                arr1_item = None
                break
            j += 1
    if arr1_item is None:
        merged_array += arr2[i-1:]
    else:
        merged_array += arr1[j-1:]
    return merged_array


if __name__ == "__main__":
    from time import perf_counter
    arr1 = [0, 3, 4, 31]
    arr2 = [4, 6, 30]
    # arr1 = list(range(10000))
    # arr2 = list(range(5000, 15000))
    # arr1 = [1, 4, 5, 23, 45, 55, 62, 74, 84,
    #         93, 100, 121, 133, 146, 189, 313, 567, 2313]
    # arr2 = [2, 5, 7, 8, 22, 33, 44, 77, 88,
    #         90, 93, 112, 146, 178, 256, 278, 421]
    expected_output = [0, 3, 4, 4, 6, 30, 31]
    t1 = perf_counter()
    output = MergeSortedArrays(arr1, arr2)
    t2 = perf_counter()
    # assert output == expected_output, f"{output}"
    output1 = MergeSortedArrays([4, 6, 30], [0, 3, 4, 31])
    print(output1)
    output2 = MergeSortedArrays([], [0, 3, 4, 4, 6, 30, 31])
    print(output2)
    output3 = MergeSortedArrays([2, 4], [2, 4])
    print(output3)

    t3 = perf_counter()
    output4 = MergeSortedArrays2(arr1, arr2)
    t4 = perf_counter()

    print(output4)
    print(t2 - t1)
    print(t4 - t3)

    t5 = perf_counter()
    output5 = MergeSortedArrays3(arr1, arr2)
    t6 = perf_counter()
    print(t6 - t5)

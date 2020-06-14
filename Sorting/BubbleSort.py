def bubbleSort(numbers: list) -> list:
    times = len(numbers) - 1
    if times == 0:  # How many loops need to be done according to the length
        return numbers
    while times > 0:
        for i in range(times):
            if numbers[i] > numbers[i + 1]:
                bigger = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = bigger
        times -= 1
    return numbers


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(bubbleSort(numbers))

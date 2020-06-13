def factorialRecursion(num):
    if num > 1:
        return num * factorialRecursion(num - 1)
    elif num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        raise ValueError('Num less than 0')


def factorialIteration(num):
    if num == 0:
        return 0
    if num < 0:
        raise ValueError('Num less than 0')
    answer = 1
    for i in range(1, num + 1):
        answer = answer * i
    return answer


if __name__ == "__main__":
    print(factorialRecursion(5))
    print(factorialIteration(5))

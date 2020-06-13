def FibonacciRecursive(num):  # O(2^N)
    if num < 0:
        raise ValueError('num is less than 0')
    if num < 2:
        return num
    return FibonacciRecursive(num - 2) + FibonacciRecursive(num - 1)


def FibonacciIterative(num):
    if num < 0:
        raise ValueError('num is less than 0')
    if num < 2:
        return num
    pre_prev = prev = answer = 1
    for i in range(2, num):
        answer = pre_prev + prev
        pre_prev = prev
        prev = answer
    return answer


# For fun
def check_input(func):
    def wrapper(num):
        if num < 0:
            raise ValueError('num is less than 0')
        return func(num)
    return wrapper


@check_input
def FibonacciRecursiveDecorator(num):  # O(2^N)
    if num < 0:
        raise ValueError('num is less than 0')
    if num < 2:
        return num
    return FibonacciRecursive(num - 2) + FibonacciRecursive(num - 1)


if __name__ == "__main__":
    import timeit
    test_fibonacci1 = 'FibonacciRecursive(30)'
    test_fibonacci2 = 'FibonacciIterative(30)'
    test_fibonacci3 = 'FibonacciRecursiveDecorator(30)'
    setup_code = """from __main__ import FibonacciRecursive,\
        FibonacciIterative, FibonacciRecursiveDecorator"""
    time1 = timeit.repeat(test_fibonacci1, setup_code, repeat=3, number=100)
    time2 = timeit.repeat(test_fibonacci2, setup_code, repeat=3, number=100)
    time3 = timeit.repeat(test_fibonacci3, setup_code, repeat=3, number=100)
    print('Recursive way:', min(time1))
    print('Iterative way:', min(time2))
    print('Recursive + decorator way:', min(time3))
    # print(FibonacciRecursive(2))
    # print(FibonacciIterative(8))

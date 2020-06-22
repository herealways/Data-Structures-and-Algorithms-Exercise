import sys
from pathlib import Path
PATH = str(Path(__file__).parent.parent)
sys.path.append(PATH)

from Recursion.Fibonacci import FibonacciIterative, FibonacciRecursive


def FibonacciDynamic():  # Top-down memoization
    cache = {}

    def Fibonacci(x):
        if x in cache:
            return cache[x]
        if x < 2:
            return x
        cache[x] = Fibonacci(x - 1) + Fibonacci(x - 2)
        return cache[x]

    return Fibonacci


def FibonacciDynamic2(x):  # Bottom-up approach
    answer = [0, 1]
    for i in range(2, x+1):
        answer.append(answer[i - 2] + answer[i - 1])
    return answer.pop()


if __name__ == "__main__":
    # print(FibonacciRecursive(35))
    # print(FibonacciIterative(35))
    # Fibo_dynamic = FibonacciDynamic()
    # print(Fibo_dynamic(35))
    # print(FibonacciDynamic2(10))
    import timeit
    test_fibonacci1 = 'FibonacciRecursive(25)'
    test_fibonacci2 = 'FibonacciIterative(25)'
    test_fibonacci3 = 'Fibo_dynamic=FibonacciDynamic(); Fibo_dynamic(25)'
    test_fibonacci4 = 'FibonacciDynamic2(25)'
    setup_code = """from __main__ import FibonacciRecursive,\
        FibonacciIterative, FibonacciDynamic, FibonacciDynamic2"""
    time1 = timeit.repeat(test_fibonacci1, setup_code, repeat=3, number=100)
    time2 = timeit.repeat(test_fibonacci2, setup_code, repeat=3, number=100)
    time3 = timeit.repeat(test_fibonacci3, setup_code, repeat=3, number=100)
    time4 = timeit.repeat(test_fibonacci4, setup_code, repeat=3, number=100)
    print('Recursive way:', min(time1))
    print('Iterative way:', min(time2))
    print('Recursive + Dynamic + Memoization way:', min(time3))
    print('Dynamic + bottom-up approach way:', min(time4))

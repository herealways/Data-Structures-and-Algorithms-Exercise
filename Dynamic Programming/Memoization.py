from time import sleep
cache0 = {}


def memoization_test0(x):
    if x in cache0:
        return cache0[x]
    print('Doing work for 1 sec...')
    sleep(1)
    result = x ** 2
    cache0[x] = result
    return result


def memoization_test1():
    cache1 = {}

    def square(x):
        if x in cache1:
            return cache1[x]
        print('Doing work for 1 sec...')
        sleep(1)
        result = x ** 2
        cache1[x] = result
        return result
    return square


if __name__ == "__main__":
    print(memoization_test0(5))
    print(memoization_test0(5))
    print('{:-^20}'.format(' '))
    memoization = memoization_test1()
    print(memoization(5))
    print(memoization(5))
    print(memoization(6))
    print(memoization(6))

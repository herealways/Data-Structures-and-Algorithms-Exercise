def reverseString(string):
    str_list = list(string)
    length = len(str_list)
    for i in range(int(length / 2)):
        temp = str_list[i]
        j = length - i - 1
        str_list[i] = str_list[j]
        str_list[j] = temp
    return ''.join(str_list)


def RecursiveReverseString(string):
    if string == "":
        return ""
    return string[-1] + RecursiveReverseString(string[:-1])


if __name__ == "__main__":
    assert reverseString('yoyo mastery') == 'yretsam oyoy'
    assert RecursiveReverseString('yoyo mastery') == 'yretsam oyoy'
    import timeit
    setup_code = 'from __main__ import reverseString, RecursiveReverseString'
    test1 = "reverseString('yoyo mastery')"
    test2 = "RecursiveReverseString('yoyo mastery')"
    time1 = timeit.repeat(test1, setup_code)
    time2 = timeit.repeat(test2, setup_code)
    print('Iterative:', min(time1))
    print('Recursive:', min(time2))

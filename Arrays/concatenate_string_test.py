string1 = 'ee' * 100000000
string2 = 'ff' * 100000000


def ConcatenateString1(str1, str2):
    return string1 + string2


def ConcatenateString2(str1, str2):
    return f'{str1}{str2}'


def ConcatenateString3(str1, str2):
    return ''.join([str1, str2])


if __name__ == "__main__":
    from time import perf_counter
    import profile

    profile.run('ConcatenateString1(string1, string2)')

    t2 = perf_counter()
    ConcatenateString1(string1, string2)
    print(perf_counter() - t2)

    t3 = perf_counter()
    ConcatenateString1(string1, string2)
    print(perf_counter() - t3)

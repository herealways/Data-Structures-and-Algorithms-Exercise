string = "Hi My Name is Andrei"
reversed_string = "ierdnA si emaN yM iH"


def ReverseString(original: str) -> str:
    if type(original) != str or len(original) < 2:
        return "Bad input!"
    my_reversed_string = ''
    for c in original:
        my_reversed_string = c + my_reversed_string
    return my_reversed_string


def ReverseString2(original: str) -> str:
    l1 = list(original)
    l1.reverse()
    return ''.join(l1)


def ReverseString3(original: str) -> str:
    l1 = []
    for c in string:
        l1.append(c)
    l1.reverse()
    return ''.join(l1)


def ReverseString4(original: str) -> str:
    s = ''
    for c in original:
        s = f'{c}{s}'
    return s


if __name__ == "__main__":
    from time import perf_counter

    t1 = perf_counter()
    assert ReverseString(string) == reversed_string
    print(perf_counter() - t1)
    t2 = perf_counter()
    assert ReverseString2(string) == reversed_string
    print(perf_counter() - t2)
    t3 = perf_counter()
    assert ReverseString3(string) == reversed_string
    print(perf_counter() - t3)
    t4 = perf_counter()
    assert ReverseString4(string) == reversed_string
    print(perf_counter() - t4)

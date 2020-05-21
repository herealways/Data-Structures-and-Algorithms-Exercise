def IfHasEqualItems(list1: list, list2: list) -> bool:
    two_list = list1 + list2
    len1 = len(two_list)
    two_set = set(two_list)
    len2 = len(two_set)
    if len1 > len2:
        return True
    return False


if __name__ == "__main__":
    print(IfHasEqualItems([[], 'b', 'c', 'x'], ['z', 'y', 'i']))
    print(IfHasEqualItems(['a', 'b', 'c', 'x'], ['z', 'y', 'x']))
    print(IfHasEqualItems([], []))

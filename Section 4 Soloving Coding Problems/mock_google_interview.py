# [1, 2, 3, 9] -> 8
# [1, 2, 4, 4] -> 8


def GetMatchingPair(arr, match_num):
    complement_set = set()
    for i in arr:
        if i in complement_set:
            return (i, match_num - i)
        else:
            complement_set.add(match_num - i)
    return False


if __name__ == "__main__":
    print(GetMatchingPair([1, 2, 3, 9], 8))
    print(GetMatchingPair([1, 2, 4, 4], 8))

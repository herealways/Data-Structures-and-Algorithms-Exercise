# Input: an array with or without recurring elements.
# Output: the first recurring character, or None.
# For example:
# Given a list [2, 5, 1, 2, 3, 5, 1, 2, 4], it should return 2
# Given a list [2, 1, 1, 2, 3, 5, 1, 2, 4], it should return 1
# Given a list [2, 3, 4, 5], it should return None
from types import GeneratorType


def find_recurring_character(elements: list):
    # Check input
    if not isinstance(elements, (list, tuple, GeneratorType)):
        raise TypeError('Except a list, tuple or a generator')
    char_set = set()
    for element in elements:
        if element in char_set:
            return element
        char_set.add(element)
    return None


if __name__ == "__main__":
    elements1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
    elements2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
    elements3 = [2, 3, 4, 5]
    assert find_recurring_character(elements1), 2
    assert find_recurring_character(elements2), 1
    assert find_recurring_character(elements3) is None
    assert find_recurring_character([]) is None

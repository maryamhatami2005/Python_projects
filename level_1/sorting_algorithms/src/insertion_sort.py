from typing import List

def insertion_sort(list: List[int]) -> List[int]:
    """
    Sorts a list using Insertion Sort algorithm

    :param list: The list to be sorted
    :return: The sorted list
    """
    n = len(list)
    for i in range(1,n):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list
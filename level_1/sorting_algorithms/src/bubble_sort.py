from typing import List

def bubble_sort(list:List[int]) -> List[int]:
    """
    Sorts a list using Selection Sort algorithm

    :param list: The list to be sorted
    :return: The sorted list
    """
    n = len(list)
    for i in range(n):
        for j in range(n-1-i):
            if list[j] > list[j+1]:
                list[j], list[j +1 ] = list[j + 1], list[j]
    return list
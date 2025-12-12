from typing import List

def selection_sort_classic(list:List[int]) -> List[int]:
    """
    Sorts a list using Selection Sort algorithm(Classical approach)

    :param list: The list to be sorted
    :return: The sorted list
    """
    for i in range(len(list)):
        min_idx = i
        for j in range(i + 1, len(list)):
            if list[i] < list[min_idx]:
                min_idx = i
            list[i], list[min_idx] = list[min_idx], list[i]
    return list

def selection_sort_pythonic(list: List[int]) -> List[int]:
    """
    Sorts a list using Selection Sort algorithm(Using python's built-ins)

    :param list: The list to be sorted
    :return: The sorted list
    """
    n = len(list)
    for i in range(n):
        minimum = min(list[i:])
        min_index = list.index(minimum, i) # start searching from position i
        list[i], list[min_index] = list[min_index], list[i]
    return list
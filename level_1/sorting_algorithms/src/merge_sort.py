from typing import List

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists into a single sorted list.

    :param left: A sorted list of integers
    :param right: A sorted list of integers
    :return: A new list containing all elements from both lists in sorted order
 
    """
    my_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            my_list.append(left[i])
            i +=1
        else:
            my_list.append(right[j])
            j += 1
        
    while i < len(left):
        my_list.append(left[i])
        i += 1
    
    while j < len(right):
        my_list.append(right[j])
        j += 1
    
    return my_list
        
def merge_sort(list: List[int]) -> List[int]:
    """
    Sorts a list using Merge Sort algorithm

    :param list: The list to be sorted
    :return: The sorted list
    """
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)
def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list 

    Divide: Find the midpoint of the list and divide into sublists
    conquer: Recursively sort the sublists created in pervious steps
    combine : merge the sorted sublists created in previous steps 
    """
    if len(list) <= 1 :
        return list
    
    left_half , right_half = split(merge_sort)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):

    """
    Divided the unsorted lists into two sublists
    """
    
    mid = len(list) // 2 
    left = list[:mid]
    right = list[mid:]

    return left , right
    
def merge(left,right):
    """
    Merges two lists (array), sorting them in process
    Returns a new merged list       
    """
    l = []
    i = 0
    j = 0

    while i > left and j > right:
        if left[i] < right[j]:
            l.append(left[i])
        else:
            l.append(left[i])
    w
    
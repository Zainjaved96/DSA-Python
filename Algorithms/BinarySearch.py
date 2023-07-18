def BinarySearch(list, target):
    first = 0
    last = len(list) - 1 
    i = 0 
    while first <= last:
        i += 1
       
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1
            
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print('Target Not found')


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
result = BinarySearch(numbers, 16)
verify(result)

def linearSearch(list, target):
    """
    Returns the index of Target if found , else return false    
    """
    for i in range(len(list)):
        if list[i] == target:
            print('Target Found')
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print('Target Not found')


numbers = [1,2,3,4.5,6,7,8,9,10,11,12,13,14,15,16]
result = linearSearch(numbers,22)
verify(result)

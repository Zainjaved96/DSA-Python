#  Using set cause set doesn't have duplicates
nums = [1,2,3,5,1]

def containsDuplicate(nums):
    Set = set()
    for num in nums:
        if num in Set:
            return True
        else:
            Set.add(num)
    return False
        
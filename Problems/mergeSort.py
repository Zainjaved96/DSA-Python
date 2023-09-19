# Merge two lists
num1 = [1,2,3,0,0,0]
num2 = [2,5,6]
 
m = 3
n = 3

# Simple Built in Method
def mergeSort(m,n, nums1,nums2):
    result_length = m+n
    nums1.extend(nums2)
    while result_length != len(nums1):
        nums1.remove(0)
    nums1.sort()

# Complicated Index using Method
def mergeSort2(m,n,nums1,nums2):
    result_length = m+n
    nums1.extend(nums2)
    while result_length != len(nums1):
        nums1.remove(0)
    nums1.sort()


mergeSort(m,n, num1, num2)
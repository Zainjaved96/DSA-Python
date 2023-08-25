nums = [1,1,2,3,4,5,6]
def removeDuplicates(nums) :
    new = []
    k = 0
    d = 0
    for num in nums:
        if num in new:
            d += 1
        else:
            new.append(num)
            k += 1

    for i in range(0,k):
        new.append("_")

    for i in range(1, k):
        nums[i] = new[i]
    return k 

removeDuplicates(nums)
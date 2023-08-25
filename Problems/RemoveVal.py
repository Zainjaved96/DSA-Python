
def removeElement(nums, val) :
    new = nums
    val_exist = True
    d = 0
    while val_exist:     
        if val in new :
            new.remove(val)
            new.append('_')
            d += 1
        else:
            val_exist = False
            
    for i in range(1, len(new)):
        nums[i] = new[i]

    return  int(len(nums) - d)
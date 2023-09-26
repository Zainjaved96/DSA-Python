# Using hashmaping value to index  then checking if target - current value is present in 
# dictionary 

def twoSum(a = [1,2,4,6,7], target = 10) :
        buffer_dict = {}
        for i in range(len(nums)):
            if target - nums[i]  in buffer_dict:
                return [buffer_dict[target - nums[i]], i]
            else:
                buffer_dict[nums[i]] = i


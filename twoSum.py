

def twoSum(nums, target):

    num_dict = dict()
    for i in range(len(nums)):
        num_dict[nums[i]] = i
    
    
    for i in range(len(nums)):
      result = target - nums[i]
      if result in num_dict and i != num_dict[result]:
        return(i,num_dict[result] )
    

    

print(twoSum([1, 2, 3], 4))        # [0, 2]
print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(twoSum([3, 2, 4], 6))        # [1, 2]
print(twoSum([3, 3], 6))           # [0, 1]
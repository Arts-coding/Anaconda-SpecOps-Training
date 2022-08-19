def contains_duplicate(nums):
    new_nums = []

    for i in range(len(nums)):
       if nums[i] not in new_nums:
           new_nums.append(nums[i])
    if len(new_nums) < len(nums):
        return True
    else:
        return False

print(contains_duplicate([1, 2, 3, 4]))
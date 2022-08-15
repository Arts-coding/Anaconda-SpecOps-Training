def sum_unique_elements(nums):
    unique_nums = []

    for i in nums:
         if i not in nums[i:]:
             unique_nums.append(i)

    res = sum(unique_nums)
    return res

print(sum_unique_elements([1, 2, 3, 2]))
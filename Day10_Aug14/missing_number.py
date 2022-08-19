def missing_number(nums):
    n = len(nums)
    for i in range(0, n + 1):
        if i not in nums:
            return i

print(missing_number([0,1]))
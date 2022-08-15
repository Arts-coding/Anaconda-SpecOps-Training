def first_last_position(nums, target):
    start = 0
    last = len(nums) - 1
    res = []

    if target not in nums:
        res = [-1, -1]

    while start <= last:
        mid = (start + last) // 2

        if nums[mid] == target:
            res.append(mid)
        if target <= nums[mid]:
            last = mid - 1
      
        else:
            start = mid + 1
    return res

print(first_last_position([5, 7, 7, 8, 8, 10], 0))
def parity_sort(nums):
    i = 0
    x = 0

    while i < len(nums):
        if nums[i] % 2 == 0:
            nums[x], nums[i] = nums[i],nums[x]  

            x += 1
        i += 1
        
    return nums
print(parity_sort([3, 2, 1, 4]))
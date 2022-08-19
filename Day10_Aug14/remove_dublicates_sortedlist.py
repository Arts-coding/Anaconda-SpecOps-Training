def rem_dublicates_sortedlist(nums):
    dub_count = 0
    new_nums = []
    
    for i in range(len(nums)):
        if nums[i] not in new_nums:
            new_nums.append(nums[i])
            
        else:
            dub_count +=1
    j = 1
    while j <= dub_count:
        new_nums.append('_')
        j += 1

    return new_nums

print(rem_dublicates_sortedlist([1, 1, 2]))

def max_consecutive_ones(nums):
        res = 0
        max_el = 0
    
        for i in range(0, len(nums)):
            if nums[i] == 1:
                res += 1
            else:
                max_el = max(res, max_el)
                res = 0

        return max(res, max_el)

print(max_consecutive_ones([1, 1, 0, 1, 0, 1]))


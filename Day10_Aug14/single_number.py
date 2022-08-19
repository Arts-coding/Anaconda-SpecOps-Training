from cmath import sin


def single_number(nums):
    res = 0
    for x in nums:
            res ^= x
    return res

print(single_number([1, 2, 3]))
def  Intersection_Two_List(nums1, nums2):
    """Get two list and  return an list of their intersection 
        
        Args:
            nums1 (_list)
            result (_list)
            nums2 (_list)"""

    result = []

    if len(nums2) <= len(nums1):
        for i in range(0, len(nums1)):
            if (nums1[i] in nums2) and (nums1[i] not in result):
                result.append(nums1[i])
    else:
        for i in range(0, len(nums2)):
            if (nums2[i] in nums1) and (nums2[i] not in result):
                result.append(nums2[i])

    return result

print(Intersection_Two_List([1, 2, 2, 1], [2, 2]))

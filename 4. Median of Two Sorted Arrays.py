def findMedianSortedArrays(nums1, nums2):
    merged_arr = nums1 + nums2
    merged_arr.sort()
    n = len(merged_arr)
    mid = n // 2
    if n % 2 == 1:
        return float(merged_arr[mid])
    else:
        return (merged_arr[mid - 1] + merged_arr[mid]) / 2.0

nums1 = [1, 3]
nums2 = [2]
print("Example 1 Output:", findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]
print("Example 2 Output:", findMedianSortedArrays(nums1, nums2))

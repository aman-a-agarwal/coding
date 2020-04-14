def binarySearch(nums, target):
    low, high = 0, len(nums) - 1
    mid = low + (high - low) // 2
    while low <= mid:
        if target > nums[mid]:
            low = mid + 1

        elif target < nums[mid]:
            high = mid - 1

        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
    return -1


a = binarySearch([1, 5, 23, 111], 111)
print(a)

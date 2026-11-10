def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert insertion_sort([3, 2, 1]) == [1, 2, 3]
assert insertion_sort([1, 2, 3]) == [1, 2, 3]
assert insertion_sort([1]) == [1]
assert insertion_sort([]) == []
print("Insertion sort test successful.")
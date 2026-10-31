def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums

assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
print("Works beautifully!")
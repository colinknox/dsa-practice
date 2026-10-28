def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                swapping = True
        end -= 1

    return nums



print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort([10, 8, 6, 4, 2]))
print(bubble_sort([9, 7, 5, 3, 1]))
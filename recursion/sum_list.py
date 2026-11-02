def sum_list(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_list(nums[1:])

assert sum_list([5, 4, 3, 2, 1]) == 15
assert sum_list([2]) == 2
assert sum_list([2, 4, 6, 8, 10]) == 30
assert sum_list([1, 2, 3]) == 6
assert sum_list([]) == 0
print("Sum List tests successful!")

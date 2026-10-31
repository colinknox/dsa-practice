def sum_list(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_list(nums[1:])

assert sum_list([]) == 0
assert sum_list([5]) == 5
assert sum_list([4, 2, 7]) == 13
assert sum_list([-1, 1]) == 0
print("All tests passed!")
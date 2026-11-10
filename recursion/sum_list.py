def sum_list(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_list(nums[1:])


assert sum_list([1, 2, 3]) == 6
assert sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
assert sum_list([100, 50, 25]) == 175
assert sum_list([11, 22, 33]) == 66
assert sum_list([3]) == 3
assert sum_list([]) == 0
print("Sum list function successful.")

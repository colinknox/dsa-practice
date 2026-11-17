def count(nums, target):
    if len(nums) == 0:
        return 0
    elif target == nums[0]:
        return 1 + count(nums[1:], target)
    else:
        return count(nums[1:], target)


assert count([2, 3, 4, 4, 9, 4, 6], 4) == 3
assert count([1, 2, 3, 4, 5], 4) == 1
assert count([3, 2, 1, 2, 3], 2) == 2
assert count([2], 2) == 1
assert count([2], 3) == 0
assert count([], 8) == 0
print("Count test successful.")
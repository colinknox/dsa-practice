def count(nums, target):
    if len(nums) == 0:
        return 0
    elif nums[0] == target:
        return 1 + count(nums[1:], target)
    else:
        return count(nums[1:], target)

        
assert count([3, 6, 7, 3, 2, 4, 5, 3, 0, 3], 3) == 4
assert count([3, 3, 0, 3, 3], 3) == 4
assert count([2, -4, -3], -3) == 1
assert count([6], 2) == 0
assert count([], 3) == 0
print("All tests pass.")
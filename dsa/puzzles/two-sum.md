# Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

Example 3:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints:

* `2 <= nums.length <= 10^4`
* `-109 <= nums[i] <= 10^9`
* `-109 <= target <= 10^9`
* `Only one valid answer exists.`

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## Solution

```py
def solve(nums, target):
    assert 2 <= len(nums) <= 10**4, "2 <= nums.length <= 10^4"
    assert all([-109 <= i <= 10**9 for i in nums]), "-109 <= nums[i] <= 10^9"
    assert -109 <= target <= 10**9, "-109 <= target <= 10^9"

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def solve2(nums, target):
    assert 2 <= len(nums) <= 10**4, "2 <= nums.length <= 10^4"
    assert all([-109 <= i <= 10**9 for i in nums]), "-109 <= nums[i] <= 10^9"
    assert -109 <= target <= 10**9, "-109 <= target <= 10^9"

    nums = sorted(nums)

    l_pointer = 0
    r_pointer = len(nums)-1

    for i in range(len(nums)):
        total = nums[l_pointer] + nums[r_pointer]

        if total > target:
            r_pointer -= 1

        if total < target:
            l_pointer += 1

        if total == target:
            return [l_pointer, r_pointer]


def solve3(nums, target):
    assert 2 <= len(nums) <= 10**4, "2 <= nums.length <= 10^4"
    assert all([-109 <= i <= 10**9 for i in nums]), "-109 <= nums[i] <= 10^9"
    assert -109 <= target <= 10**9, "-109 <= target <= 10^9"

    #complement = [target - nums[i] for i in range(len(nums))]

    d = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in d:
            return [d[complement], i] # return first and current match

            d[nums[i]] = i

nums = [2,7,11,15]
target = 9

# 1.33 µs ± 170 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
%timeit solve1(nums, target)

# 1.58 µs ± 169 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
%timeit solve2(nums, target)

# 1.22 µs ± 130 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
%timeit solve3(nums, target)
```
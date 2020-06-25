# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:  # From leetcode discussion
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0

        for n in nums:
            temp = prev1
            prev1 = max(n + prev2, prev1)
            prev2 = temp
        return prev1


def rob(nums: List[int]) -> int:  # Recursive + memoization
    length = len(nums)
    if length == 0:
        return 0
    if length <= 2:
        return max(nums)
    memo = {}

    def helper(nums: List[int], index: int) -> int:
        if index < 0:
            return 0
        if index in memo:
            return memo[index]
        memo[index] = max(helper(nums, index - 2) + nums[index],
                          helper(nums, index - 1))
        return memo[index]
    return helper(nums, length - 1)


def rob2(nums: List[int]) -> int:  # Tabulation
    if len(nums) == 0:
        return 0
    prev2 = prev1 = 0
    for i in nums:
        temp = prev1
        prev1 = max(prev2 + i, prev1)
        prev2 = temp
    return prev1


if __name__ == "__main__":
    s = Solution()
    s.rob([1, 9, 2, 3, 15])
    print(rob([1, 9, 2, 3, 15]))
    print(rob2([1, 9, 2, 3, 15]))

"""
 * Leetcode 47: Given a collection of numbers, nums, that might contain duplicates,
   return all possible unique permutations in any order.

 * Date: 31/10/2024
 * @param {List[int]} nums
 * @return {List[List[int]]}
 *
 *  Example 1:
    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
    [1,2,1],
    [2,1,1]]

    Example 2:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                used[i] = True
                backtrack(path + [nums[i]], used)
                used[i] = False
        backtrack([], [False] * len(nums))
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([1,1,2])) # [[1,1,2],[1,2,1],[2,1,1]]
    print(sol.permuteUnique([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


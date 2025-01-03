"""
 * Leetcode 18: Given an array nums of n integers, 
   return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
   0 <= a, b, c, d < n
   a, b, c, and d are distinct.
   nums[a] + nums[b] + nums[c] + nums[d] == target
   You may return the answer in any order.

 * Date: 16/10/2024
 * @param {list[int]} nums
 * @param {int} target
 * @return {list[list[int]]}
 * 
 *  Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    
    Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print(solution.fourSum([2, 2, 2, 2, 2], 8)) # [[2, 2, 2, 2]]


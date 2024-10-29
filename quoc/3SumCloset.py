"""
 * Leetcode 16: Given an integer array nums and an integer target, 
   find three integers in nums such that the sum is closest to target.
   Return the sum of the three integers.

 * Date: 14/10/2024
 * @param {list[int]} nums
 * @param {int} target
 * @return {int}
 * 
 *  Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
    Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1,2,1,-4], 1)) # 2
    print(solution.threeSumClosest([0,0,0], 1)) # 0

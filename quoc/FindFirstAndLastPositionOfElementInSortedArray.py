"""
 * Leetcode 34: Given an array of integers nums sorted in non-decreasing order, 
   find the starting and ending position of a given target value.
   If target is not found in the array, return [-1, -1].
   You must write an algorithm with O(log n) runtime complexity.

 * Date: 23/10/2024
 * @param {List[int]} nums
 * @param {int} target
 * @return {List[int]}
 * 
 *  Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    
    Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
    
    Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
    
    def binarySearch(self, nums: List[int], target: int, leftBias: bool) -> int:
        l, r = 0, len(nums) - 1
        i = -1
        
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1 
        return i

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5,7,7,8,8,10], 8)) # [3,4]
    print(solution.searchRange([5,7,7,8,8,10], 6)) # [-1,-1]
    print(solution.searchRange([], 0)) # [-1,-1]


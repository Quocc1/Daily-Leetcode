"""
 * Leetcode 46: Given an array nums of distinct integers, return all the possible permutations
   You can return the answer in any order.

 * Date: 30/10/2024
 * @param {list[int]} nums
 * @return {list[list[int]]}
 * 
 *  Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
    Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Example 3:
    Input: nums = [1]
    Output: [[1]]
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            for perm in self.permute(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + perm)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(sol.permute([0,1])) # [[0,1],[1,0]]
    print(sol.permute([1])) # [[1]]

"""
 * Leetcode 78: Given an integer array nums of unique elements, return all possible subsets (the power set).
 * Date: 03/10/2024
 * @param {int[]} nums
 * @return {List[List[int]]}
 * 
 *  Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    
    Example 2:
    Input: nums = [0]
    Output: [[],[0]]
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(solution.subsets([0])) # [[],[0]]
    
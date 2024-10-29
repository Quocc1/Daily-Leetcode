"""
 * Leetcode 45: You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
   Each element nums[i] represents the maximum length of a forward jump from index i. 
   In other words, if you are at nums[i], you can jump to any nums[i + j] where:
   0 <= j <= nums[i] and
   i + j < n
   Return the minimum number of jumps to reach nums[n - 1]. 
   The test cases are generated such that you can reach nums[n - 1].

 * Date: 29/10/2024
 * @param {List[int]} nums
 * @return {int}
 * 
 *  Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
    Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([2,3,1,1,4])) # 2
    print(sol.jump([2,3,0,1,4])) # 2

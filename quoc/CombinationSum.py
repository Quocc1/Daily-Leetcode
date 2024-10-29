"""
 * Leetcode 39: Given an array of distinct integers candidates and a target integer target, 
   return a list of all unique combinations of candidates where the chosen numbers sum to target. 
   You may return the combinations in any order.

 * Date: 26/10/2024
 * @param {List[int]} candidates
 * @param {int} target
 * @return {List[List[int]]}
 * 
 *  Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.
    
    Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
    
    Example 3:
    Input: candidates = [2], target = 1
    Output: []
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()
                
        result = []
        backtrack(0, target, [])
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]
    print(solution.combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
    print(solution.combinationSum([2], 1)) # []

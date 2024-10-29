"""
 * Leetcode 40: Given a collection of candidate numbers (candidates) and a target number (target), 
   find all unique combinations in candidates where the candidate numbers sum to target.
   Each number in candidates may only be used once in the combination.

 * Date: 27/10/2024
 * @param {List[int]} candidates
 * @param {int} target
 * @return {List[List[int]]}
 * 
 *  Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]
    
    Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
                
        result = []
        backtrack(0, target, [])
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2([10,1,2,7,6,1,5], 8)) # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(solution.combinationSum2([2,5,2,1,2], 5)) # [[1,2,2],[5]]

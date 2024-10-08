"""
 * Leetcode 64: Given a m x n grid filled with non-negative numbers, 
   find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
 * Date: 06/10/2024
 * @param {List[List[int]]} grid
 * @return {int}
 * 
 *  Example 1:
    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
    
    Example 2:
    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]])) # 7
    print(solution.minPathSum([[1,2,3],[4,5,6]])) # 12


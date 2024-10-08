"""
 * Leetcode 63: You are given an m x n integer array grid. 
   There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
   The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
   The robot can only move either down or right at any point in time.
 * Date: 07/10/2024
 * @param {List[List[int]]} grid
 * @return {int}
 * 
 *  Example 1:
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right
    
    Example 2:
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])) # 2
    print(solution.uniquePathsWithObstacles([[0,1],[0,0]])) # 1



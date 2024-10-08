"""
 * Leetcode 48: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). 
 * Date: 08/10/2024
 * @param {List[List[int]]} matrix
 * @return {None}
 * 
 *  Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
    
    Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
    print(solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] 


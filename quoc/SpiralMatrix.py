"""
 * Leetcode 54: Given an m x n matrix, return all elements of the matrix in spiral order.

 * Date: 04/11/2024
 * @param {List[List[int]]} matrix
 * @return {List[int]}
 *
 *  Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]

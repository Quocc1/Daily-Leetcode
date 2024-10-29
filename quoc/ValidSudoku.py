"""
 * Leetcode 36: Determine if a 9 x 9 Sudoku board is valid. 
   Only the filled cells need to be validated according to the following rules:
   - Each row must contain the digits 1-9 without repetition.
   - Each column must contain the digits 1-9 without repetition.
   - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

 * Date: 24/10/2024
 * @param {List[List[str]]} board
 * @return {bool}
 * 
 *  Example 1:
    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true
    
    Example 2:
    Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
    Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not self.isValid(board, i, j):
                        return False
        return True
    
    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        for i in range(9):
            if board[row][i] == board[row][col] and i != col:
                return False
            if board[i][col] == board[row][col] and i != row:
                return False
        for i in range(3):
            for j in range(3):
                if board[row // 3 * 3 + i][col // 3 * 3 + j] == board[row][col] and (row // 3 * 3 + i) != row and (col // 3 * 3 + j) != col:
                    return False
        return True
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]])) # True
    print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]])) # False


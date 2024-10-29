"""
 * Leetcode 6: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
    (you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
 * Date: 09/10/2024
 * @param {str} s
 * @param {int} numRows
 * @return {str}
 * 
 *  Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    Example 3:
    Input: s = "A", numRows = 1
    Output: "A"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row] += char
            current_row += direction

            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

        return ''.join(rows)

if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3)) # "PAHNAPLSIIGYIR"
    print(solution.convert("PAYPALISHIRING", 4)) # "PINALSIGYAHRPI"
    print(solution.convert("A", 1)) # "A"

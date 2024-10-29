"""
 * Leetcode 22: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 * Date: 18/10/2024
 * @param {int} n
 * @return {List[str]}
 * 
 *  Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    
    Example 2:
    Input: n = 1
    Output: ["()"]
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s: str, left: int, right: int):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)
        
        result = []
        backtrack("", 0, 0)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
    print(sol.generateParenthesis(1)) # ["()"]

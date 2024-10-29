"""
 * Leetcode 17: Given a string containing digits from 2-9 inclusive, 
   return all possible letter combinations that the number could represent.
   Return the answer in any order.

 * Date: 15/10/2024
 * @param {str} digits
 * @return {list[str]}
 * 
 *  Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    Example 2:
    Input: digits = ""
    Output: []
    
    Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]
"""

from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        self.backtrack(digits, 0, "", result, digit_to_char)
        return result

    def backtrack(self, digits: str, index: int, path: str, result: List[str], digit_to_char: Dict[str, str]) -> None:
        if index == len(digits):
            result.append(path)
            return
        for char in digit_to_char[digits[index]]:
            self.backtrack(digits, index + 1, path + char, result, digit_to_char)

if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(solution.letterCombinations("")) # []
    print(solution.letterCombinations("2")) # ["a","b","c"]


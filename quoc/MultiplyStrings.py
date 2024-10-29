"""
 * Leetcode 43: Given two non-negative integers num1 and num2 represented as strings, 
   return the product of num1 and num2, also represented as a string.

 * Date: 28/10/2024
 * @param {str} num1
 * @param {str} num2
 * @return {str}
 * 
 *  Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"
    
    Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply("2", "3")) # "6"
    print(solution.multiply("123", "456")) # "56088"


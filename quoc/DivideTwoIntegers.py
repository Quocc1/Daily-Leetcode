"""
 * Leetcode 29: Given two integers dividend and divisor, divide two integers without using multiplication, 
   division, and mod operator.
   The integer division should truncate toward zero, which means losing its fractional part. 
   For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
   Return the quotient after dividing dividend by divisor.

 * Date: 20/10/2024
 * @param {int} dividend
 * @param {int} divisor
 * @return {int}
 * 
 *  Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = 3.33333.. which is truncated to 3.
    
    Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = -2.33333.. which is truncated to -2.
"""

from typing import List


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if abs(divisor) == 1:
            return dividend * divisor
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple
        return sign * result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(10, 3)) # 3
    print(sol.divide(-2147483648, -1)) # 2147483647 

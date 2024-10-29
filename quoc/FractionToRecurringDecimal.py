"""
 * Leetcode 166: Given two integers representing the numerator and denominator of a fraction, 
   return the fraction in string format.
 * Date: 04/10/2024
 * @param {int} numerator
 * @param {int} denominator
 * @return {str}
 * 
 *  Example 1:
    Input: numerator = 1, denominator = 2
    Output: "0.5"

    Example 2:
    Input: numerator = 2, denominator = 1
    Output: "2"

    Example 3:
    Input: numerator = 4, denominator = 333
    Output: "0.(012)"
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        result = []
        if (numerator < 0) != (denominator < 0):
            result.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        integer_part = numerator // denominator
        result.append(str(integer_part))
        result.append('.')
        
        numerator %= denominator
        
        remainder_map = {}
        
        while numerator != 0:
            if numerator in remainder_map:
                result.insert(remainder_map[numerator], '(')
                result.append(')')
                break
            remainder_map[numerator] = len(result)
            numerator *= 10
            result.append(str(numerator // denominator))
            numerator %= denominator
        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()
    print(solution.fractionToDecimal(1, 2)) # "0.5"
    print(solution.fractionToDecimal(2, 1)) # "2"
    print(solution.fractionToDecimal(4, 333)) # "0.(012)"


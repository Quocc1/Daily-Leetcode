"""
 * Leetcode 12: Given an integer num, convert it to a roman numeral.

 * Date: 12/10/2024
 * @param {int} num
 * @return {str}
 * 
 *  Example 1:
    Input: num = 3749
    Output: "MMMDCCXLIX"
    Explanation:
    3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
    700 = DCC as 500 (D) + 100 (C) + 100 (C)
    40 = XL as 10 (X) less of 50 (L)
    9 = IX as 1 (I) less of 10 (X)
    Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
    
    Example 2:
    Input: num = 58
    Output: "LVIII"
    Explanation:
    50 = L
    8 = VIII
    
    Example 3:
    Input: num = 1994
    Output: "MCMXCIV"
    Explanation:
    1000 = M
    900 = CM
    90 = XC
    4 = IV
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = [(1000, 'M')]
        hundreds = [(900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C')]
        tens = [(90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X')]
        ones = [(9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        
        roman_table = thousands + hundreds + tens + ones
        
        result = ''
        for value, symbol in roman_table:
            while num >= value:
                result += symbol
                num -= value
                
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(3749)) # "MMMDCCXLIX"
    print(solution.intToRoman(58)) # "LVIII"
    print(solution.intToRoman(1994)) # "MCMXCIV"

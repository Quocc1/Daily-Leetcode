"""
 * Leetcode 50: Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 * Date: 02/11/2024
 * @param {float} x
 * @param {int} n
 * @return {float}
 *
 *  Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

    Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        return x * self.myPow(x * x, (n - 1) // 2)

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2, 10)) # 1024
    print(sol.myPow(2.1, 3)) # 9.261
    print(sol.myPow(2, -2)) # 0.25



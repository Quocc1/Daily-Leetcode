"""
 * Leetcode 1497: Check If Array Pairs Are Divisible by k
 * Date: 02/10/2024
 * @param {int[]} arr
 * @param {int} k
 * @return {boolean}
 * 
 *  Example 1:
    Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
    Output: true
    Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

    Example 2:
    Input: arr = [1,2,3,4,5,6], k = 7
    Output: true
    Explanation: Pairs are (1,6),(2,5) and(3,4).

    Example 3:
    Input: arr = [1,2,3,4,5,6], k = 10
    Output: false
    Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
"""

from collections import defaultdict
from typing import List


class Solution:
  def canArrange(self, arr: List[int], k: int) -> bool:
    reminders = defaultdict(int)
    for i in range(0, len(arr)):
      reminders[arr[i] % k] += 1
      
    for reminder in reminders:
      if reminder == 0:
        if reminders[reminder] % 2 != 0:
          return False
      else:
        if reminders[reminder] != reminders[k - reminder]:
          return False
    return True
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.canArrange([1,2,3,4,5,10,6,7,8,9], 5)) # True
    print(solution.canArrange([1,2,3,4,5,6], 7)) # True
    print(solution.canArrange([1,2,3,4,5,6], 10)) # False
    print(solution.canArrange([75,5,-5,75,-2,-3,88,10,10,87], 85)) # True

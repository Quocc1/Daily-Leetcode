/**
 * Leetcode 1497. Check If Array Pairs Are Divisible by k
 * @param {number[]} arr
 * @param {number} k
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
 */
var canArrange = function (arr, k) {
  let remainderCounters = {};

  for (const num of arr) {
    const remainder = ((num % k) + k) % k;
    remainderCounters[remainder] = (remainderCounters[remainder] || 0) + 1;
  }

  console.log(remainderCounters);

  for (const key in remainderCounters) {
    const index = parseInt(key);
    if (index === 0) {
      if (remainderCounters[index] % 2 !== 0) {
        return false;
      }
    } else {
      const j = k - index;
      if (remainderCounters[index] !== remainderCounters[j]) {
        return false;
      }
    }
  }

  return true;
};

// let arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9];
// let k = 5;
// console.log(canArrange(arr, k));

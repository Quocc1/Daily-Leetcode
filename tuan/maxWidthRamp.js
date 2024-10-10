/**
 * Leetcode 921. Minimum Add to Make Parentheses Valid
 * Date: 10/10/2024
 * Level: Medium
 * @param {number[]} nums
 * @return {number}
 */
var maxWidthRamp = function (nums) {
  let stackOfi = [];

  for (let i = 0; i < nums.length; i++) {
    if (
      stackOfi.length === 0 ||
      nums[i] < nums[stackOfi[stackOfi.length - 1]]
    ) {
      stackOfi.push(i);
    }
  }

  let maxWidthRamp = 0;

  for (let j = nums.length - 1; j >= 0; j--) {
    while (stackOfi.length && nums[j] >= nums[stackOfi[stackOfi.length - 1]]) {
      const minIdxItem = stackOfi.pop();
      maxWidthRamp = Math.max(maxWidthRamp, j - minIdxItem);
    }
  }

  return maxWidthRamp;
};

const input = [6, 0, 8, 2, 1, 5];
console.log(maxWidthRamp(input));

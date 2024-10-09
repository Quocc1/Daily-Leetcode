/**
 * Leetcode 921. Minimum Add to Make Parentheses Valid
 * Date: 09/10/2024
 * Level: Medium
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function (s) {
  let countOpen = 0;
  let countClose = 0;

  for (const char of s) {
    if (char === "(") {
      countOpen++;
    } else {
      if (countOpen > 0) {
        countOpen--;
      } else {
        countClose++;
      }
    }
  }
  return countOpen + countClose;
};
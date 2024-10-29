"""
 * Leetcode 24: Given a linked list, swap every two adjacent nodes and return its head. 
 You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 * Date: 19/10/2024
 * @param {ListNode} head
 * @return {ListNode}
 * 
 *  Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

    Example 2:
    Input: head = []
    Output: []

    Example 3:
    Input: head = [1]
    Output: [1]

    Example 4:
    Input: head = [1,2,3]
    Output: [2,1,3]
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        prev, current = dummy, head
        
        while current and current.next:
            next_pair = current.next.next
            second = current.next

            second.next = current
            current.next = next_pair
            prev.next = second
            prev = current
            current = next_pair
        return dummy.next

if __name__ == "__main__":
    sol = Solution()
    print(sol.swapPairs([1,2,3,4])) # [2,1,4,3]
    print(sol.swapPairs([])) # []
    print(sol.swapPairs([1])) # [1]
    print(sol.swapPairs([1,2,3])) # [2,1,3]

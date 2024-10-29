"""
 * Leetcode 19: Given the head of a linked list, remove the nth node from the end of the list and return its head.

 * Date: 17/10/2024
 * @param {ListNode} head
 * @param {int} n
 * @return {ListNode}
 * 
 *  Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    
    Example 2:
    Input: head = [1], n = 1
    Output: []
    
    Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for _ in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)) # [1,2,3,5]
    print(solution.removeNthFromEnd(ListNode(1), 1)) # []
    print(solution.removeNthFromEnd(ListNode(1, ListNode(2)), 1)) # [1]

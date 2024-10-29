"""
 * Leetcode 102: Given the root of a binary tree, 
    return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 * Date: 05/10/2024
 * @param {TreeNode} root
 * @return {List[List[int]]}
 * 
 *  Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    
    Example 2:
    Input: root = [1]
    Output: [[1]]
    
    Example 3:
    Input: root = []
    Output: []
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.levelOrder([3,9,20,None,None,15,7])) # [[3],[9,20],[15,7]]
    print(solution.levelOrder([1])) # [[1]]
    print(solution.levelOrder([])) # []



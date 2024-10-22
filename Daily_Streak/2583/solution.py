from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        # BFS kullanarak her seviyeyi gezeceğiz
        queue = deque([root])
        level_sums = []
        
        while queue:
            level_size = len(queue)
            level_sum = 0
 
            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(level_sum)
        
        level_sums.sort(reverse=True)

        if k <= len(level_sums):
            return level_sums[k-1]
        else:
            return -1

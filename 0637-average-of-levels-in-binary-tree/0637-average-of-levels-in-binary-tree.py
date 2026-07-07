from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            size = len(queue)
            levelsum = 0

            for i in range(size):
                node = queue.popleft()
                levelsum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(levelsum / float(size))

        return res
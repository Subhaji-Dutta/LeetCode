from collections import deque

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            level_size = len(q)
            level_sum = 0

            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level_sum / float(level_size))

        return ans
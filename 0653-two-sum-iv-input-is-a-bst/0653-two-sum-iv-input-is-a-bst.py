from collections import deque

class Solution(object):
    def findTarget(self, root, k):
        if not root:
            return False

        seen = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if k - node.val in seen:
                return True

            seen.add(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTarget(self, root, k):
        seen = set()

        def f(root):
            if not root:
                return False

            if k - root.val in seen:
                return True

            seen.add(root.val)

            return f(root.left) or f(root.right)

        return f(root)
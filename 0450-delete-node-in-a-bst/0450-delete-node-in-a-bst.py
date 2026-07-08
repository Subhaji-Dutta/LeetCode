# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        rightChild = root.right
        lastRight = root.left

        while lastRight.right:
            lastRight = lastRight.right
        
        lastRight.right = rightChild
        return root.left

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        
        if root.val == key:
            return self.helper(root)
        
        curr = root

        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.helper(curr.left)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.helper(curr.right)
                    break
                else:
                    curr = curr.right

        return root
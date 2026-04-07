# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Solve

class Solution:
    def buildTree(self, preorder, inorder):
        # map value -> index for quick lookup
        index_map = {val: i for i, val in enumerate(inorder)}

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # find root in inorder
            mid = index_map[root_val]
            left_size = mid - in_start

            # build left subtree
            root.left = helper(
                pre_start + 1,
                pre_start + left_size,
                in_start,
                mid - 1
            )

            # build right subtree
            root.right = helper(
                pre_start + left_size + 1,
                pre_end,
                mid + 1,
                in_end
            )

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
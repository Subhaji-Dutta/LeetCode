# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

# Example 1:


# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
# Example 2:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in head is in the range [0, 2 * 104].
# -105 <= Node.val <= 105
# Solve

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        # get length
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        self.head = head

        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2

            left = build(l, mid - 1)

            root = TreeNode(self.head.val)
            root.left = left
            self.head = self.head.next

            root.right = build(mid + 1, r)
            return root

        return build(0, n - 1)
        
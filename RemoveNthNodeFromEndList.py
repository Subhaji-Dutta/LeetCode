# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 
# Solve

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = slow = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove nth node
        slow.next = slow.next.next

        return dummy.next
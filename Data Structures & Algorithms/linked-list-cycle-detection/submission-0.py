# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # start slow and fast pointer at the same position
        slow, fast = head, head

        # we are going to be shifting our fast and slow pointers
        # while fast and fast.next are not null because we need to make sure that 
        # fast.next is not null because we are shifting fast by 2 for each iteration
        while fast and fast.next:
            # check if there is a cycle
            # shift slow pointer by 1
            slow = slow.next

            # shift fast pointer by 2
            fast = fast.next.next
            
            # if they meet each other then there exists a cycle and we can return True
            if slow == fast:
                return True
            
        # meaning fast reached the end of the linked list before it reached the slow pointer so there is no cycle
        return False 
        
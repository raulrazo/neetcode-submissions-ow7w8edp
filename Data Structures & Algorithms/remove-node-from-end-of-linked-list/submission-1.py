# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node at the beginning to make sure left pointer end up in right spot
        # right node at intialized at n place so it ends up in the right spot
        # loop to move right node to the n place
        # loop and shift l and r pointers until right node = null

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right != None:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy node with next pointer at head of the list
        dummy = ListNode(0, head)

        left = dummy

        # put right pointer at head + n through a loop
        right = head

        while n > 0 and right:
            right = right.next 

            # decrement n by 1 because once n = 0, that means we shifted by the correct amount
            n -= 1

        # keep shifting both pointers until right reaches the end of the list
        while right:
            left = left.next
            right = right.next

        # delete the node by updating the left node's next pointer
        left.next = left.next.next 

        # we know dummy is at the head so we just return dummy.next
        return dummy.next
        
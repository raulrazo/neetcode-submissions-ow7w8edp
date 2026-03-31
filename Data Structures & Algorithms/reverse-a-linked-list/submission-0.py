# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize pointers
        prev = None
        curr = head

        # keep going until we reach the end of the list
        # while current is not null we are going to reverse the pointers
        while curr:
            # temp variable called nxt so when we update curr.next, we can preserve it
            nxt = curr.next 
            curr.next = prev # current's next is set to previous
            # shift pointers
            prev = curr # update previous and set it to curr
            curr = nxt

        # return result which we know is stored in previous when this loop stops executing
        return prev
            
        
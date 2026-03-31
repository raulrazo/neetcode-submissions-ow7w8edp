# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to not have to deal with any edge cases when inserting into our new resulting linked list
        dummy = ListNode()

        # and our current node is going to be pointing at the position that we are going to be inserting our new node into
        cur = dummy

        # initialize the carry value that we will be maintaining
        carry = 0

        # while either of the list have a digit
        # handle the edge case where we have a carry leftover after our lists are done so while carry is non null then we want to continue our loop 
        while l1 or l2 or carry:
            # get the digits
            # get the digit from l1 only if l1 is not null, if null then set it to our default value of 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # compute our new digit
            val = v1 + v2 + carry

            # we could potentially have a new carry so we do this shit
            carry = val // 10
            # if our value is greater than 10 then we want only the 1s place digit
            val = val % 10

            # now we insert our digit into our new list
            cur.next = ListNode(val)

            # update our pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
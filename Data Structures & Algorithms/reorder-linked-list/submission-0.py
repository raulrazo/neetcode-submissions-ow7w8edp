# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # intialize slow and fast pointers to find the middle of the list
        slow = head
        fast = head.next

        # while fast is not null and has not reached the end of the linked list:
        while fast and fast.next:
            # shift slow and fast pointers
            slow = slow.next
            fast = fast.next.next

        # now we have the beginning of the second half of the list, slow.next
        second = slow.next

        # set slow.next to null now because we are splitting them into two different lists
        slow.next = None

        # now we reverse the second half of the list
        # set previous to null, we gotta keep track of it anyway
        prev = None
        # while second is not null
        while second:
            # store temporary variable for second.next
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            # idk this shit, this is reversing a linked list ig

        # now we are going to merge the two halves of the list

        # the beginning of the second half is going to be the previous pointer because after the while loop is 
        # done, second is going to be set to null, but previous is going to be set to the last node that we visited 
        # and that previous is going to be the head of the new list
        second = prev

        # first half is going to start at the head
        first = head

        # keep going until one of the pointers is null
        # we know the second half could be shorter than the first half so we do while second is not null
        while second:
            # store the next nodes in temp variables because we know we are going to be breaking those links
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            
            # tmp1 b/c we are inserting the second node in between first and first.next 
            second.next = tmp1

            # shift our pointers
            first = tmp1
            second = tmp2
        
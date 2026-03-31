# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if the input linked list is empty then we can't do any rotations so we just return that empty linked list
        if not head:
            return head

        # get the length of the linked list and also get the tail in the process
        # initially the length is going to be 1 because we know we have at least one node that is not null
        # and the tail is initially going to be set to the head node because we know for sure the head node is not null
        length, tail = 1, head

        # while there is a next node for us to iterate through
        while tail.next:
            # we are going to move to that position in the linked list 
            # and increment our length by 1
            tail = tail.next
            length += 1

        # now we take k and mod it by the input length to reduce it to a number that is less than length
        k = k % length

        # if k is equal to 0 then the number of rotations is a multiple of the length of the linked list
        # and we do not need to do any rotations on it so we can just return it
        if k == 0:
            return head

        # now we move to the pivot and actually perform the rotate
        # start at the head node
        cur = head
        # iterate until we reach pivot point and we do that by using the formula from the explanation
        for i in range(length - k - 1):
            # every iteration we are going to move to the next position
            cur = cur.next
        # now that we exit that loop, current is at the node where we are going to do the pivot rotation thing at

        # make the new head which is going to be cur.next
        newHead = cur.next

        # now we update cur.next and set it to null because this is going to be the pivot position and the new end of the linked list
        # this is basically detaching the last k nodes
        cur.next = None

        # now we set tail.next to be the new beginning of our linked list
        tail.next = head

        return newHead
        
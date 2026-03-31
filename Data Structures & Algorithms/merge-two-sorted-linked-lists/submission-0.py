# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node
        dummy = ListNode()
        tail = dummy

        # while both of the list are non empty AKA not null
        while list1 and list2: 
            if list1.val < list2.val: # if the value of list 1 is less than the value of list 2
                # take list 1 value and insert it into our tail
                tail.next = list1
                list1 = list1.next # update our list one pointer
            else:
                tail.next = list2 # insert list2 value
                list2 = list2.next # update our list two pointer
            
            # tail pointer is updated regardless of which node is inserted into our list
            tail = tail.next

        # if one of the list is empty but the other isn't
        # find non-empty list and insert at the end of our result

        if list1:
            tail.next = list1 # taking the remaining portion of l1 and inserting it into the end of the list
        elif list2:
            tail.next = list2

        return dummy.next

        
        
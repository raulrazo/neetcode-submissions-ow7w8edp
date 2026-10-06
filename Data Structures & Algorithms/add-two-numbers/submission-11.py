# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # create dummy node to eliminate special edge case logic
        # for initializing head of resulting linked list.
        dummy = ListNode()

        # sets a traveral pointer cur starting at dummy so we can
        # move cur and still use dummy to refer to our resulting
        # linked list.
        cur = dummy

        # tracks the overflow to the next decimal place.
        carry = 0

        # continues iterating as long as there is work to do.
        while l1 or l2 or carry:
            # handles unequal list lengths with else statements.
            # gets values we are going to sum together.

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # sums the current numbers and carry if there is one.
            val = v1 + v2 + carry

            # extract carry digit by extracting tens digit to 
            # carry over to the next place. 
            carry = val // 10

            # mod val by 10 ti get single digit remainder for this
            # current place.
            val = val % 10

            # allocate new node with computed digit and links it
            # after cur so we can keep traversing.
            cur.next = ListNode(val)

            # iterate all the pointers to the next position 
            # so we can move on to next digits place.
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # dummy.next points to the true head of the constructed
        # result list at this point, so return it.
        return dummy.next

        # Time and Space Complexity

        # O(max(m, n)) time comeplexity where m in numbers of
        # nodes in l1 and n is number of nodes in l2 because we
        # are going to do as many iterations as the longest list.

        # O(1) space complexity because we don't use any extra
        # data structures unless you count output linked list.
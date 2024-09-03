# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:

            first_N = current.next
            second_N = first_N.next 

            ##swapping
            first_N.next = second_N.next
            second_N.next = first_N
            current.next = second_N

            ##next_swap
            current = first_N
        
        return dummy.next
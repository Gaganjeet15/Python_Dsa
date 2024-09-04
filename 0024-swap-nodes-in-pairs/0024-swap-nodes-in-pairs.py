# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        point = dummy

        while point.next and point.next.next:
            first = point.next 
            second = first.next

            first.next = second.next
            second.next = first

            point.next = second

            point = first

        return dummy.next
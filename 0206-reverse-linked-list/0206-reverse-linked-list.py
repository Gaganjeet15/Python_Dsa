# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:  # Check if the list is empty
            return head 

        previous =  None ## pointer pointing to null
        present = head ## present is pointing at head

        while present: ##while present
            forward = present.next ## forward will be pointer to next
            present.next = previous
            previous = present
            present = forward
        return previous

    
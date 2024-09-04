# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = None
        old_head = head
        prev = None
        count = 0
        current = old_head

        while current:
            if current.val != 0:
                count +=current.val
            else:
                if count > 0:
                    new_node = ListNode(count)

                    if new_head is None:
                        new_head = new_node
                        prev = new_node
                    else:
                        prev.next = new_node
                        prev = new_node
                
                count = 0
            current = current.next
        return new_head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        head = [0,1,2,3]
        holder -> 0 -> 1 -> 2 -> 3 → null
        prev      c    temp
        """
        prev = None
        c = head

        while c is not None:
            temp = c.next
            c.next = prev
            prev = c
            c = temp
        return prev




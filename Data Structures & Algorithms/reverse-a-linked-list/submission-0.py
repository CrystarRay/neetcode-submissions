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
                p
        """

        p = head
        arr= []
        
        while p is not None: 
            arr.append(p.val)
            p = p.next 
        arr.reverse()
        
        new_head = None
        curr = None

        for val in arr:
            node = ListNode(val)
            if new_head is None:
                new_head = node
                curr = node
            else:
                curr.next = node
                curr = curr.next

        return new_head


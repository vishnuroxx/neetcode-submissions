# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find size
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        n = (size - n) + 1

        if n == 1:
            return head.next if head else None
        else:

            curr = head
            while curr and n > 2: 
                curr = curr.next
                n -= 1
                
            print(curr.val)

            if curr and curr.next:
                curr.next = curr.next.next
            
            return head
                


        
        
        
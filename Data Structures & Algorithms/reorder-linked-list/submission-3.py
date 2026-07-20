# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find length of the linked list
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next 
        
        # find the mid-point
        mid_index = (N // 2)
        # find mid node
        mid = head
        
        while  mid_index > 0:
            mid = mid.next 
            mid_index -= 1
          
        
        # reverse edges of all nodes after this 
        ahead = mid.next 
        prev = None  
        while ahead:
            temp = ahead.next
            ahead.next = prev 
            prev = ahead   
            ahead = temp
            

        # traverse and update according 
        curr = head 
        while prev:
            temp = curr.next 
            curr.next = prev
            prev = prev.next
            curr.next.next = temp
            curr = temp
        
        mid.next = None
        

  
            

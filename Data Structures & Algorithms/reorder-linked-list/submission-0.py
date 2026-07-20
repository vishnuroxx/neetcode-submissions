# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head 
        while curr:
            stack.append(curr) # O(n)
            curr = curr.next

        curr = head 
        temp = -1
        nextNode = -2
        while stack and stack[-1] != curr: # O(n)
            temp = stack.pop()
            
            nextNode = curr.next
            curr.next = temp
            
            if nextNode != temp:
                temp.next = nextNode
            else:
                curr = temp
                break 
   

            curr = nextNode
          
        curr.next = None



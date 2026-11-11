"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        nodes = []
        curr = head
        
        while curr != None:
            new_node = Node(curr.val)
            new_node.next = curr.next 
            curr.next = new_node
            curr = curr.next.next

        
        result = head.next 

        curr = head
        while curr != None:
            
            if curr.random:
                curr.next.random = curr.random.next 
            curr = curr.next.next 
 

        curr = head
        while curr != None:
            duplicate = curr.next 
            curr.next = curr.next.next 
            duplicate.next = curr.next.next if curr.next else None
       
            curr = curr.next
       

        return result


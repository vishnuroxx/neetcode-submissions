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
        nodes = []
        hash = {}
        curr = head
        while curr != None:
            new_node = Node(curr.val)
            hash[curr] = new_node
            nodes.append(new_node)
            curr = curr.next

       
        curr = head
        idx = 0
        while curr != None:
            nodes[idx].next = hash[curr.next] if curr.next else None
            nodes[idx].random = hash[curr.random] if curr.random else None
            idx += 1
            curr = curr.next

        return nodes[0] if nodes else None
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
        otc = {None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            otc[cur] = copy
            cur = cur.next
        
        cur = head

        while cur:
            copy = otc[cur]
            copy.next = otc[cur.next]
            copy.random = otc[cur.random]
            cur = cur.next
        
        return otc[head]
        
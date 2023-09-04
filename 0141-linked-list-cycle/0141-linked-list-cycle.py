# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set({})
        cur = head
        while(cur != None):
            if(cur in node_set):
                return True
            node_set.add(cur)
            cur = cur.next
            
            
        
        return False
        
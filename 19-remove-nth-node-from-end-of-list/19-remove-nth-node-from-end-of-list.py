# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        m = len(nodes) - n
        if len(nodes) == 1:
            return
        if m == 0:
            return nodes[1]
        elif m == len(nodes)-1:
            nodes[m-1].next = None
        else:
            nodes[m-1].next = nodes[m+1]
        return nodes[0]
            
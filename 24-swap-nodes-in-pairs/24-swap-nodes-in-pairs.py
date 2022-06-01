# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        tmp = head
        while tmp:
            nodes.append(tmp)
            tmp = tmp.next
            
        for i in range(0,len(nodes),2):
            if i+1 < len(nodes):
                nodes[i],nodes[i+1] = nodes[i+1],nodes[i]
        head,tmp = None,None
        for i in range(len(nodes)):
            val,nxt = nodes[i].val,nodes[i].next
            newNode = ListNode(val)
            if head:
                tmp.next = newNode
                tmp = newNode
            else:
                head = newNode
                tmp = newNode
        return head
                
            
            
            
        
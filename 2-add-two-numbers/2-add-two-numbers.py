# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        IntegerListNode1 = int(self.ListNode2String(l1))
        IntegerListNode2 = int(self.ListNode2String(l2))
        stringNum = list(str(IntegerListNode1+IntegerListNode2))[::-1]
        
        startNode = ListNode(stringNum[0])
        tmpNode = startNode
        for i in range(1,len(stringNum)):
            curNode = ListNode(stringNum[i])
            tmpNode.next = curNode
            tmpNode = curNode
        return startNode
        
        
    def ListNode2String(self,listNode):
        if listNode.next == None:
            return str(listNode.val)
        return self.ListNode2String(listNode.next) + str(listNode.val)
    

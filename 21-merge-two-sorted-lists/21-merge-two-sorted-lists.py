# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while list1 and list2:
            if list1.val <= list2.val:
                tmp.append(list1.val)
                list1 = list1.next
            else:
                tmp.append(list2.val)
                list2 = list2.next

        while list1:
            tmp.append(list1.val)
            list1 = list1.next
        
        while list2:
            tmp.append(list2.val)
            list2 = list2.next
        header = ListNode()
        tmpNode = header
        for t in tmp:
            newNode = ListNode(t)
            tmpNode.next = newNode
            tmpNode = newNode
        return header.next
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        beg = ListNode(0, head)
        current = head
        prev = beg
        
        while current != None:
            if current.next != None and current.next.val < current.val:
                while prev.next != None and prev.next.val < current.next.val:
                    prev = prev.next
                
                nextNode = prev.next
                prev.next = current.next
                current.next = current.next.next
                prev.next.next = nextNode
                prev = beg
            else:
                current = current.next
                
        return beg.next
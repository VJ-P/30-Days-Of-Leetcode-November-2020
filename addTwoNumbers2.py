# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = "", ""
        
        while(l1 != None):
            num1 += str(l1.val)
            l1 = l1.next
        
        while(l2 != None):
            num2 += str(l2.val)
            l2 = l2.next
            
        num1 = int(num1)
        num2 = int(num2)
        ans = list(str(num1 + num2))
        
        head = ListNode(int(ans[0]), None)
        curr = head
        for i in range(1, len(ans)):
            curr.next = ListNode(int(ans[i]), None)
            curr = curr.next
        
        return head
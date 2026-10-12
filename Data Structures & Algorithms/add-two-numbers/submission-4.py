# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1 or l2:
            if l1:
                num1 = str(l1.val) + num1
                l1 = l1.next
            else:
                num1 = str(0) + num1

            if l2:
                num2 = str(l2.val) + num2
                l2 = l2.next
            else:
                num2 = str(0) + num2

        retStr = int(num1) + int(num2)
        retStr = str(retStr)

        i = len(retStr) - 1
        head = ListNode(int(retStr[i]))
        i -= 1
        cur = head

        while i >= 0:
            cur.next = ListNode(int(retStr[i]))
            cur = cur.next
            i -= 1
        
        return head
        

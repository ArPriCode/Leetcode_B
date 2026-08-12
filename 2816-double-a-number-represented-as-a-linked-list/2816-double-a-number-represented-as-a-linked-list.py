# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        if head.val > 4:
            head = ListNode(0, head)
        
        temp = head
        while temp is not None:
            temp.val = (temp.val * 2) % 10
            if temp.next is not None and temp.next.val > 4:
                temp.val += 1
            
            temp = temp.next
        
        return head
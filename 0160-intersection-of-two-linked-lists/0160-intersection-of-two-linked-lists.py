# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1!=p2 :
            p1 = headB if p1 == None else p1.next 
            p2 = headA if p2 == None else p2.next
            
        return p1
            
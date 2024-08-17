# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0 :
            return head
        temp = head
        len = 1 
        while temp.next :
            len+=1
            temp = temp.next 
        temp.next = head
        k = k%len
        end = len - k 
        while end : 
            temp = temp.next 
            end-=1
        head = temp.next 
        temp.next = None 
        return head
        
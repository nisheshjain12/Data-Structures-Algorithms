# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        f,s=head,head
        temp=None
        while f and f.next:
            temp=s
            f=f.next.next
            s=s.next
        temp.next=temp.next.next
        return head
    
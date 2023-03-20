/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if(head.next == null) return null;
        ListNode first = head;
        ListNode second = head;
        ListNode temp = null;
        
        while( first!=null && first.next!=null){
            temp=second;
            first=first.next.next;
            second=second.next;
        }
        temp.next=temp.next.next;
        return head;
    }
}

    
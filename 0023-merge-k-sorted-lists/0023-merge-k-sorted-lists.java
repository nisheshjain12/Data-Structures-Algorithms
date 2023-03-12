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
    public ListNode mergeKLists(ListNode[] lists) {
        List<Integer> array = new ArrayList<>();
        for (ListNode ln:lists){
            while(ln!=null){
                array.add(ln.val);
                ln=ln.next;
            }
        }
        Collections.sort(array);
        ListNode head = new ListNode(0);
        ListNode h=head;
        for(int i:array){
            ListNode t=new ListNode(i);
            h.next=t;
            h=h.next;
        }
        h.next=null;
        return head.next;

    }
}
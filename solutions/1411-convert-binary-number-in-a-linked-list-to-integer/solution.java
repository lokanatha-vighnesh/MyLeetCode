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
    public int getDecimalValue(ListNode head) {
        ListNode temp1 = head;
        ListNode temp2 = head;
        int answer = 0;
        int i=0;
        while(temp1.next != null){
            temp1 = temp1.next;
            i++;
        }
        while(temp2 != null){
            answer += (temp2.val * Math.pow(2,i--));
            temp2 = temp2.next;
        }
        return answer;
    }
}

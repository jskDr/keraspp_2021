public class ListNode {
    private int data;
    private ListNode next;
    public ListNode() {
        data = 0;
        next = null;
    }
    public ListNode(int data, ListNode next) {
        this.data = data;
        this.next = next;
    }
    public void setData(int data) {
        this.data = data;
    }    
    public int getData() {
        return data;
    }
}

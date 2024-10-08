class Solution {
    public Node removeAllDuplicates(Node head) {
        // code here
        if(head.next==null)return head;
        Node ans=new Node(-1),prev=head;
        Node temp=ans;
        head=head.next;
        int count=1;
        while(head!=null){
            if(prev.data==head.data)count++;
            else if(count==1){
                temp.next=prev;
                temp=temp.next;
            }
            else count=1;
            prev=head;
            head=head.next;
        }
        if(count==1)temp.next=prev;
        else
        temp.next=null;
        return ans.next;
    }
}
/* structure for a node
class Node {
 public:
  int data;
  Node *next;

  Node(int x){
      data = x;
      next = NULL;
  }
}; */

class Solution {
  public:
    Node* sortedInsert(Node* head, int data) {
        // code here
        Node *t = new Node(data);
        
        Node *curr = head, *fut = head->next;
        while(fut != head){
            if(data < fut->data && data >= curr->data){
                curr->next = t;
                t->next = fut;
                return head;
            }
            curr = fut;
            fut = fut->next;
        }
        //insert at start
        if(data < fut->data){
            curr->next = t;
            t->next = fut;
            head  = t;
            return head;
        }
        
        // insert at end
        if(data >= curr->data){
            curr->next = t;
            t->next = fut;
        }
        
        return head ; 
        
        
   

    }
};

/*
class Node {
    int data;
    Node left, right;
    Node(int val){
        data = val;
        left = right = null;
    }
}
*/

class Solution {
    // Function to return a list containing the postorder traversal of the tree.
    ArrayList<Integer> postOrder(Node root) {
        // Your code goes here
        ArrayList<Integer> arr=new ArrayList<>();
        helper(root, arr);
        return arr;
    }
    void helper(Node root,ArrayList<Integer> arr){
        if(root==null){
            return ;
        }
        helper(root.left,arr);
        helper(root.right,arr);
        arr.add(root.data);
    }
}


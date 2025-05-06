class Solution {
  public:
    vector<int> leftView(Node *root) {
        
        if(root == NULL){
            return {};
        }
        queue<Node*> q;
        q.push(root);
        vector<int> ans;
        
        while(!q.empty()){
            int n = q.size();
            Node* node = NULL;
            
            while(n--){
                node = q.front();
                q.pop();
                if(node->right){
                    q.push(node->right);
                }
                if(node->left){
                    q.push(node->left);
                }
            }
            ans.push_back(node->data);
        }
        return ans;
    }
};

class Solution {
  public:
    vector<int> findSpiral(Node* root) {
        // code here
        vector<int> ans;
        queue<Node*> q;
        q.push(root);
        
        bool isOpp = true;
        
        while(!q.empty()){
            int n = q.size();
            
            vector<int> temp;
            while(n--){
                auto z = q.front();
                q.pop();
                temp.push_back(z->data);
                
                if(z->left)
                    q.push(z->left);
                if(z->right)
                    q.push(z->right);
                
            }
            
            if(isOpp)
                reverse(temp.begin(), temp.end());
            
            isOpp = !isOpp;
            for(auto x : temp){
                ans.push_back(x);
            }
            
        }
        
        
        return ans;
    }
};


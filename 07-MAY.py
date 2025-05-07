class Solution {
    vector<vector<int>> paths;
    void f(Node * node , vector<int> & cur_path){
        if(node == nullptr) return ; 
        cur_path.push_back(node->data); 
        if(node->left == nullptr && node->right == nullptr){
            paths.push_back(cur_path) ; 
        }
        f(node->left , cur_path) ; 
        f(node->right , cur_path) ; 
        cur_path.pop_back() ; 
    }
  public:
    vector<vector<int>> Paths(Node* root) {
        vector<int> cur_paths ; 
        f(root , cur_paths) ; 
        return paths ;
    }
};

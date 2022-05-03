class Solution {
public:
    void sol(Node* root,vector<int> &ans){
        if(root==NULL){
            return;
        }
       
        for(auto node : root->children){
            sol(node,ans);
        }
         ans.push_back(root->val);
    }
    
    vector<int> postorder(Node* root) {
        vector<int> ans;
        sol(root,ans);
        return ans;
    }
};

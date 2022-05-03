class Solution {
public:
    void sol(Node* root,vector<int> &ans){
        if(root==NULL){
            return;
        }
        ans.push_back(root->val);
        for(auto node : root->children){
            sol(node,ans);
        }
    }
    
    vector<int> preorder(Node* root) {
        vector<int> ans;
        sol(root,ans);
        return ans;
    }
};

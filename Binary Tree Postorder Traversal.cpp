class Solution {
public:
     vector<int> v;
    void lnr(TreeNode *root){
        if(root == NULL){
            return;
        }
        lnr(root->left);
        
        lnr(root->right);
        v.push_back(root->val);
    }
    vector<int> postorderTraversal(TreeNode* root) {
        lnr(root);
        return v;
    }
};

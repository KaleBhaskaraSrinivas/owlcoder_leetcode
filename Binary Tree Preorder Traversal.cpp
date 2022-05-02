class Solution {
public:
     vector<int> v;
    void lnr(TreeNode *root){
        if(root == NULL){
            return;
        }
        v.push_back(root->val);
        lnr(root->left);
 
        lnr(root->right);
    }
    vector<int> preorderTraversal(TreeNode* root) {
         lnr(root);
        return v;
    }
};

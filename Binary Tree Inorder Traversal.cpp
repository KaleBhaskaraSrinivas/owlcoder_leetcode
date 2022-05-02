class Solution {
public:
    vector<int> v;
    void lnr(TreeNode *root){
        if(root == NULL){
            return;
        }
        lnr(root->left);
        v.push_back(root->val);
        lnr(root->right);
    }
    // Function to return a list containing 

    vector<int> inorderTraversal(TreeNode* root) {
        lnr(root);
        return v;
    }
};

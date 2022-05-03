class Solution {
public:
    int sum = 0;
    void leaves(TreeNode* root) {
        if(root==NULL)
            return;
        if(root -> left and !root->left->left and !root -> left -> right) {
            sum += root -> left -> val;
        }
        leaves(root -> left);
        leaves(root -> right);
    }
    int sumOfLeftLeaves(TreeNode* root) {
        leaves(root);
        return sum;
    }
};

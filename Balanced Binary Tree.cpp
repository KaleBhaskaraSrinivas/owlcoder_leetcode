class Solution {
public:
    bool f=true;
    int height(TreeNode *root){
        if(root==NULL){
            return 0;
        }
        int l = height(root->left);
        int r = height(root->right);
        if(abs(l - r) > 1){
          f = false;  
        } 
        return max(l, r) + 1;
    }
    bool isBalanced(TreeNode* root) {
        height(root);
       return f;
    }
};

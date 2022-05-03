class Solution {
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if(root1==NULL and root2==NULL)
            return 0;
        if(root1==NULL)
            return root2;
        if(root2==NULL)
            return root1;
        root1->val=root1->val+root2->val;
        root1->left=mergeTrees(root1->left, root2->left);
        root1->right=mergeTrees(root1->right, root2->right);
        return root1;
    }
};

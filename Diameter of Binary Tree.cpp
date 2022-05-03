class Solution {
public:
    int res=0;
    int Diameter(TreeNode* root){
        if(root==NULL){
            return 0;
        }
        int l=Diameter(root->left);
        int r=Diameter(root->right);
        res=max(res,l+r);
        return 1+max(l,r);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int k= Diameter(root);
        return res;
    }
};

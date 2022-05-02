class Solution {
public:
     bool find(TreeNode* root, int tSum, int sum){
        if(root==NULL) return false;
        if(!root->left and !root->right){
            if(root->val+sum == tSum){
                return true;
            }else return false;
        } 
        return (find(root->left, tSum, root->val+sum) || find(root->right,tSum, root->val+sum)) ;
    }
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root==NULL){
            return false;
        }
       return find(root, targetSum, 0);
    }
};

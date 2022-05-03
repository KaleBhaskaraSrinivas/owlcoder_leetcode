class Solution {
public:
     void dfs(TreeNode* root, string& result) {
         if(root==NULL){
             return;
         }
        result += to_string(root->val);
        if(!root->left and !root->right){
            return;
        }
        result += '(';
        dfs(root->left, result);
        result += ')';           
        if(root->right)
        {
            result += '('; 
            dfs(root->right, result);
            result += ')';           
        }      
    }
    string tree2str(TreeNode* root) {
        string result = "";
        dfs(root, result);
        return result;
    }
};

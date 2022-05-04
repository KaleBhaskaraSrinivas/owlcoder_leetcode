class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>ans;
        if(root==NULL){
            return {};
        }
        queue<TreeNode*>q;
        q.push(root);
        
    while(!q.empty()){
        int size=q.size();
        vector<int>row(size);
        for(int i=0;i<size;i++){
            root=q.front();
            q.pop();
            row[i]=(root->val);
            if(root->left){
                q.push(root->left);
            }
            if(root->right){
                q.push(root->right);
            }
        }
        ans.push_back(row);
        }
        return ans;
    }
    
};

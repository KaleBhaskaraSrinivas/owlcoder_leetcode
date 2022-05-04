class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>ans;
        if(root==NULL){
            return {};
        }
        queue<TreeNode*>q;
        q.push(root);  
        int flag=1;
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
        if(flag==1){
            ans.push_back(row);
            flag=0;
        }
        else if(flag==0){
            reverse(row.begin(),row.end());
            ans.push_back(row);
            flag=1;
        }
        }
        return ans; 
    }
};

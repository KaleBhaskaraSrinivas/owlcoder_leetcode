class Solution {
public:
    vector<vector<int>>ans;
    void CheckTarget(int ind,int target, int n, vector<int>&candidates,vector<int>&ds)
    {
        if(ind==n){
            if(target==0){
                ans.push_back(ds);
            }
            return;
        }
        if(candidates[ind]<=target){
            ds.push_back(candidates[ind]);
            CheckTarget(ind,target-candidates[ind],n,candidates,ds);
            ds.pop_back();
        }
        CheckTarget(ind+1,target,n,candidates,ds);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        int n=candidates.size();
        vector<int>ds;
        CheckTarget(0,target,n,candidates,ds);
        return ans;
        
    }
};

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
            CheckTarget(ind+1,target-candidates[ind],n,candidates,ds);
            ds.pop_back();
        }
        CheckTarget(ind+1,target,n,candidates,ds);
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        int n=candidates.size();
        vector<int>ds;
        sort(candidates.begin(),candidates.end());
        int count=0;
        for(auto it: candidates){
            if(it==1){
                count++;
            }
        }
        if(count==candidates.size() and target<=count){
            vector<int>v(target,1);
            ans.push_back(v);
            return ans;
        }
        CheckTarget(0,target,n,candidates,ds);
        sort(ans.begin(),ans.end());
        ans.erase(unique(ans.begin(),ans.end()),ans.end());
        return ans;
        
    }
};
        

void Permutations(int n,vector<int>arr,vector<int>&ds,vector<int> vis,vector<vector<int>>&b){
    if(n==ds.size())
    {
        b.push_back(ds);
        return;
    }
    for(int i=0;i<n;i++)
    {
        if(vis[i]==0)
        {
            vis[i]=1;
            ds.push_back(arr[i]);
            Permutations(n,arr,ds,vis,b);
            vis[i]=0;
            ds.pop_back();
        }
    }
}
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        
    int n=nums.size();
    vector<int>ds;
    vector<int>vis(n,0);
    vector<vector<int>>b;
    Permutations(n,nums,ds,vis,b);
    sort(b.begin(),b.end());
    b.erase(unique(b.begin(),b.end()),b.end());
        return b ;
    }
};



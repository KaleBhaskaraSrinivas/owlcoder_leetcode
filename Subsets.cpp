class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>vec;
        int n=nums.size();
        for(int i=0;i<(1<<n);i++)
        {
            vector<int>ve;
            for(int j=0;j<n;j++)
            {
                if(i& (1<<j))
                {
                    ve.push_back(nums[j]);
                }
            }
            vec.push_back(ve);
        }
       return vec;
    }
};


class Solution {
public:
    void rec(int ind,vector<vector<int>> &ans,vector<int>nums,vector<int>&temp)
    {
        if(ind==nums.size())
        {
            ans.push_back(temp);
            return ;
        }
        temp.push_back(nums[ind]);
        rec(ind+1,ans,nums,temp);
        temp.pop_back();
        rec(ind+1,ans,nums,temp);
    }
    vector<vector<int>> subsets(vector<int>& nums) 
    {
       vector<vector<int>>ans;
        vector<int>temp;
        rec(0,ans,nums,temp);
        return ans;
    }
};

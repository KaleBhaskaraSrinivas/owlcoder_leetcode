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

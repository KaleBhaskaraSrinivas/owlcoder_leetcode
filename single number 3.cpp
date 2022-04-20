class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int>p;
        unordered_map<int, int>ump;
        for(int i=0;i<nums.size();i++)
             ump[nums[i]]++;
        for(auto i : ump)
        {
            if(i.second == 1)
             p.push_back(i.first);
        } 
        sort(p.begin(),p.end());
        return p;
        
    }
};

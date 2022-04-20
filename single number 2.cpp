class Solution {
public:
      int singleNumber(vector<int>& nums) {
        int p;
        unordered_map<int, int>ump;
        for(int i=0;i<nums.size();i++)
             ump[nums[i]]++;
        for(auto i : ump)
        {
            if(i.second == 1)
             p=i.first;
        } 
        return p;
        
    }
};

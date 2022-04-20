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


class Solution {
public:
      int singleNumber(vector<int>& nums) {
          int first=0;
          int second=0;
          for(auto i : nums)
          {
          first=first^i & (~second);
          second=second^i & (~first);
          }
          return first;  
    }
};

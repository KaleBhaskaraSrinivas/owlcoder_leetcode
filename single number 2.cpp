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



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = sorted(nums)
        for i in range(0,len(l)-2,3):
            if l[i]!=l[i+1] :
                return l[i]
        return l[-1]



        

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



class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int ans=0;
        for(auto it:nums){
            ans^=it;
        }
        int p=1;
        int i=1;
        while(1){
            if(ans & i ){
                break;
            }
            p++;
            i=i<<1;
        }
        int res1=0;
        int res2=0;
        for(auto x:nums){
            if(x & (1<<(p-1))){
                res1^=x;
            }
            else{
                res2^=x;
            }
        }
        return {res1,res2};
    }
};










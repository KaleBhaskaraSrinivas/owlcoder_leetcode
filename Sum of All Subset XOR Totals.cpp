class Solution {
public:
    int sum=0;
    void solve(vector<int>& nums,int i,int x){
        if(i==nums.size()) sum+=x;
        else {
            solve(nums,i+1,x^nums[i]);
            solve(nums,i+1,x);
        }
        
    }
    int subsetXORSum(vector<int>& nums) {
        solve(nums,0,0);
        return sum;
    }
};

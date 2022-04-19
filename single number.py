class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            x^=i
        return x

      
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int x=0;
        for(int i=0;i<nums.size();i++){
            x=x^nums[i];
        }
       return x; 
    }
};



        

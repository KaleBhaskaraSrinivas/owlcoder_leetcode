class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=len(nums)
        nums=sorted(nums,reverse=True)
        return (nums[0]-1)*(nums[1]-1)
        

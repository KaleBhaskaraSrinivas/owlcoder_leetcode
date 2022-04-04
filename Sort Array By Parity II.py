class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for i in range(len(nums)):
            if nums[i]%2:
                odd.append(nums[i])
            else: 
                even.append(nums[i])
        nums[0::2], nums[1::2] = even, odd
        return nums
        
